from langgraph.graph import StateGraph, END

from state import TicketState
from classifier import TicketClassifier
from response_generator import ResponseGenerator
from ticketing.client import TicketingClient

classifier = TicketClassifier()
generator = ResponseGenerator()
ticketing_client = TicketingClient()

def classify_ticket(state: TicketState):
    ticket = state["ticket"]
    result = classifier.classify(ticket)

    return {
        "classification": result
    }

def route_ticket(state: TicketState):
    escalation = state["classification"]["escalation"]

    if escalation.lower() == "yes":
        return "escalate"

    return "respond"

def generate_response(state: TicketState):
    ticket = state["ticket"]

    result = generator.generate_response(ticket)

    return {
        "response": result["response"],
        "sources": result["sources"],
        "escalation": False
    }

# def escalate_ticket(state: TicketState):
#     classification = state["classification"]

#     reason = classification.get(
#         "reason",
#         "Ticket requires human assistance."
#     )

#     return {
#         "response": (
#             "This ticket has been escalated "
#             "to a human support agent."
#         ),
#         "sources": [],
#         "escalation": True
#     }

def escalate_ticket(state: TicketState):
    ticket = state["ticket"]
    classification = state["classification"]
    result = ticketing_client.create_ticket(
        customer_ticket=ticket,
        category=classification["category"],
        priority=classification["priority"],
        sentiment=classification["sentiment"],
        reason=classification["reason"]
    )

    return {
        "response": (
            "Your ticket has been escalated "
            "to our human support team."
        ),

        "sources": [],
        "escalation": True,
        "ticket_id": result["ticket_id"],
        "ticket_status": result["status"],
        "assigned_to": result["assigned_to"]
    }

workflow = StateGraph(TicketState)

workflow.add_node(
    "classify",
    classify_ticket
)

workflow.add_node(
    "respond",
    generate_response
)

workflow.add_node(
    "escalate",
    escalate_ticket
)

workflow.set_entry_point("classify")

workflow.add_conditional_edges(
    "classify",
    route_ticket,
    {
        "respond": "respond",
        "escalate": "escalate"
    }
)

workflow.add_edge(
    "respond",
    END
)

workflow.add_edge(
    "escalate",
    END
)

graph = workflow.compile()