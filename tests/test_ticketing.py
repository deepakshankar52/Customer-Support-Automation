from ticketing.client import TicketingClient

client = TicketingClient()

result = client.create_ticket(
    customer_ticket="Someone hacked my account.",
    category="Security",
    priority="Critical",
    sentiment="Angry",
    reason="Potential account compromise."
)

print("\nTicket Created Successfully")
print("=" * 50)

print("Ticket ID:", result["ticket_id"])
print("Status:", result["status"])
print("Assigned To:", result["assigned_to"])
print("Priority:", result["priority"])