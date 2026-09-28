from classifier import TicketClassifier

classifier = TicketClassifier()

# ticket = """
# I forgot my password and cannot log in.
# """

ticket = """
Someone hacked my account and changed my email.
"""

result = classifier.classify(ticket)

print(result)