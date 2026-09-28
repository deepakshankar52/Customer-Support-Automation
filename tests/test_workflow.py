from workflow import graph

# ticket = """
# I forgot my password and cannot login.
# """

ticket = """
Someone hacked my account and changed my email.
I cannot access my account anymore.
"""

result = graph.invoke(
    {
        "ticket": ticket
    }
)


print("\n" + "=" * 60)
print("TICKET")
print("=" * 60)

print(result["ticket"])


print("\n" + "=" * 60)
print("CLASSIFICATION")
print("=" * 60)

print(result["classification"])


print("\n" + "=" * 60)
print("RESPONSE")
print("=" * 60)

print(result["response"])


print("\n" + "=" * 60)
print("ESCALATION")
print("=" * 60)

print(result["escalation"])


print("\n" + "=" * 60)
print("SOURCES")
print("=" * 60)

for source in result["sources"]:
    print(source)


print("\n" + "=" * 60)
print("TICKETING INFORMATION")
print("=" * 60)

if result.get("escalation"):
    print("Ticket ID:", result.get("ticket_id"))
    print("Status:", result.get("ticket_status"))
    print("Assigned To:", result.get("assigned_to"))
