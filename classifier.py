import json
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import classification_prompt

from dotenv import load_dotenv
load_dotenv()

class TicketClassifier:

    def __init__(self):

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    def classify(self, ticket):

        messages = classification_prompt.format_messages(
            ticket=ticket
        )

        response = self.llm.invoke(messages)

        result = response.content.strip()

        if result.startswith("```"):
            result = result.replace("```json", "")
            result = result.replace("```", "").strip()

        return json.loads(result)