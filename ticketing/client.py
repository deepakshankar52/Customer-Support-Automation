import requests

class TicketingClient:
    def __init__(self, base_url="http://127.0.0.1:8000"):
        self.base_url = base_url

    def create_ticket(
        self,
        customer_ticket,
        category,
        priority,
        sentiment,
        reason
    ):
        
        payload = {
            "customer_ticket": customer_ticket,
            "category": category,
            "priority": priority,
            "sentiment": sentiment,
            "reason": reason
        }

        response = requests.post(
            f"{self.base_url}/tickets",
            json=payload,
            timeout=10
        )

        response.raise_for_status()

        return response.json()