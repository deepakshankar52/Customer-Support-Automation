# from fastapi import FastAPI
# from pydantic import BaseModel
# from uuid import uuid4

# app = FastAPI(
#     title="Customer Support Ticketing API",
#     description="Mock ticketing API for Customer Support Automation",
#     version="1.0"
# )

# class TicketRequest(BaseModel):
#     customer_ticket: str
#     category: str
#     priority: str
#     sentiment: str
#     reason: str

# @app.post("/tickets")
# def create_ticket(ticket: TicketRequest):
#     ticket_id = f"TICKET-{str(uuid4())[:8].upper()}"

#     return {
#         "ticket_id": ticket_id,
#         "status": "Escalated",
#         "assigned_to": "Human Support Team",
#         "category": ticket.category,
#         "priority": ticket.priority,
#         "sentiment": ticket.sentiment,
#         "reason": ticket.reason
#     }

# @app.get("/health")
# def health_check():
#     return {
#         "status": "Ticketing API is running"
#     }


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from uuid import uuid4
import sqlite3
from pathlib import Path


app = FastAPI(
    title="Customer Support Ticketing API",
    description="Mock ticketing API for Customer Support Automation",
    version="1.0"
)


# SQLite database location
DB_PATH = Path(__file__).resolve().parent / "tickets.db"


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            ticket_id TEXT PRIMARY KEY,
            customer_ticket TEXT NOT NULL,
            status TEXT NOT NULL,
            assigned_to TEXT NOT NULL,
            category TEXT NOT NULL,
            priority TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            reason TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


class TicketRequest(BaseModel):
    customer_ticket: str
    category: str
    priority: str
    sentiment: str
    reason: str


@app.on_event("startup")
def startup_event():
    init_db()


@app.post("/tickets")
def create_ticket(ticket: TicketRequest):

    ticket_id = f"TICKET-{str(uuid4())[:8].upper()}"

    status = "Escalated"
    assigned_to = "Human Support Team"

    conn = get_db_connection()

    conn.execute(
        """
        INSERT INTO tickets (
            ticket_id,
            customer_ticket,
            status,
            assigned_to,
            category,
            priority,
            sentiment,
            reason
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            ticket_id,
            ticket.customer_ticket,
            status,
            assigned_to,
            ticket.category,
            ticket.priority,
            ticket.sentiment,
            ticket.reason
        )
    )

    conn.commit()
    conn.close()

    return {
        "ticket_id": ticket_id,
        "status": status,
        "assigned_to": assigned_to,
        "category": ticket.category,
        "priority": ticket.priority,
        "sentiment": ticket.sentiment,
        "reason": ticket.reason
    }


@app.get("/tickets/{ticket_id}")
def get_ticket(ticket_id: str):

    conn = get_db_connection()

    ticket = conn.execute(
        "SELECT * FROM tickets WHERE ticket_id = ?",
        (ticket_id,)
    ).fetchone()

    conn.close()

    if ticket is None:
        raise HTTPException(
            status_code=404,
            detail=f"Ticket {ticket_id} not found"
        )

    return dict(ticket)


@app.get("/health")
def health_check():
    return {
        "status": "Ticketing API is running"
    }