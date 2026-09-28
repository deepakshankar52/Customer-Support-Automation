from langchain_core.prompts import ChatPromptTemplate

classification_prompt = ChatPromptTemplate.from_template("""
You are an AI customer support ticket classifier.

Analyze the ticket and return ONLY a valid JSON object.

Categories:
- Authentication
- Billing
- Refund
- Technical Support
- Account Recovery
- General Inquiry
- Security
- Other

Priority:
- Low
- Medium
- High
- Critical

Sentiment:
- Positive
- Neutral
- Frustrated
- Angry

Escalation Rules:

Return "Yes" if:
- Security issue
- Account hacked
- Legal complaint
- Data loss
- Payment fraud
- Customer extremely angry

Otherwise return "No".

Return JSON only in this format:

{{
    "category":"",
    "priority":"",
    "sentiment":"",
    "escalation":"",
    "reason":""
}}

Ticket:

{ticket}
""")


response_prompt = ChatPromptTemplate.from_template(
"""
You are an AI Customer Support Assistant.

Your responsibilities:

- Answer only using the provided company documents.
- Never make up information.
- If the documents don't contain the answer, politely state that the information is unavailable.
- Keep the response professional, concise, and customer-friendly.
- Provide step-by-step instructions whenever appropriate.

Customer Ticket:

{ticket}

Retrieved Knowledge:

{context}

Generate the best customer support response.
"""
)