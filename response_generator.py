from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI

# from embeddings import LocalEmbeddings
from embeddings import get_embedding_model
from prompts import response_prompt

import os
from dotenv import load_dotenv
load_dotenv()

class ResponseGenerator:

    def __init__(self):

        # self.embedding_model = LocalEmbeddings()
        self.embedding_model = get_embedding_model()

        self.vector_db = FAISS.load_local(
            "vector_store",
            self.embedding_model,
            allow_dangerous_deserialization=True
        )

        self.retriever = self.vector_db.as_retriever(
            search_kwargs={"k": 3}
        )

        self.llm = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=0,
            google_api_key=os.getenv("GOOGLE_API_KEY")
        )

    # def generate_response(self, ticket):

    #     docs = self.retriever.invoke(ticket)

    #     context = "\n\n".join(
    #         doc.page_content
    #         for doc in docs
    #     )

    #     messages = response_prompt.format_messages(
    #         ticket=ticket,
    #         context=context
    #     )

    #     response = self.llm.invoke(messages)

    #     return {
    #         "response": response.content,
    #         "documents": docs
    #     }

    def generate_response(self, ticket):

        # Retrieve relevant documents
        docs = self.retriever.invoke(ticket)

        # Create context for the LLM
        context = "\n\n".join(
            doc.page_content
            for doc in docs
        )

        # Format prompt
        messages = response_prompt.format_messages(
            ticket=ticket,
            context=context
        )

        # Generate response
        response = self.llm.invoke(messages)

        # Extract source information
        sources = []

        for doc in docs:
            sources.append(
                {
                    "source": doc.metadata.get("source"),
                    "page": doc.metadata.get("page")
                }
            )

        return {
            "response": response.content,
            "sources": sources
        }