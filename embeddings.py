# from langchain_core.embeddings import Embeddings
# from sentence_transformers import SentenceTransformer


# class LocalEmbeddings(Embeddings):
#     def __init__(self):
#         self.model = SentenceTransformer(
#             "BAAI/bge-small-en-v1.5"
#         )

#     def embed_documents(self, texts):
#         embeddings = self.model.encode(
#             texts,
#             normalize_embeddings=True
#         )
#         return embeddings.tolist()

#     def embed_query(self, text):
#         embedding = self.model.encode(
#             text,
#             normalize_embeddings=True
#         )
#         return embedding.tolist()


import os

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings

load_dotenv()

def get_embedding_model():
  return OpenAIEmbeddings(
    model = "text-embedding-3-small",
    api_key = os.getenv("OPENAI_API_KEY")
  )

