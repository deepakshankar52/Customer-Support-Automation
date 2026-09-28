from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI(
    title="Customer Support Ticketing API",
    description="Mock ticketing API for Customer Support Automation",
    version="1.0"
)

class TicketRequest(BaseModel):
    customer_ticket: str
    category: str
    priority: str
    sentiment: str
    reason: str

@app.post("/tickets")
def create_ticket(ticket: TicketRequest):
    ticket_id = f"TICKET-{str(uuid4())[:8].upper()}"

    return {
        "ticket_id": ticket_id,
        "status": "Escalated",
        "assigned_to": "Human Support Team",
        "category": ticket.category,
        "priority": ticket.priority,
        "sentiment": ticket.sentiment,
        "reason": ticket.reason
    }

@app.get("/health")
def health_check():
    return {
        "status": "Ticketing API is running"
    }