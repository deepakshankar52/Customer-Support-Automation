from typing import TypedDict

class TicketState(TypedDict):
    ticket: str
    classification: dict
    response: str
    sources: list
    escalation: bool
    ticket_id: str
    ticket_status: str
    assigned_to: str