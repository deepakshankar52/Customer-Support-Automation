from langchain_community.vectorstores import FAISS

# from embeddings import LocalEmbeddings
from embeddings import get_embedding_model

# embedding_model = LocalEmbeddings()
embedding_model = get_embedding_model()

db = FAISS.load_local(
    "vector_store",
    embedding_model,
    allow_dangerous_deserialization=True
)

retriever = db.as_retriever(
    search_kwargs={"k": 3}
)

query = "How can I reset my password?"

docs = retriever.invoke(query)

for i, doc in enumerate(docs, start=1):
    print(f"\nDocument {i}\n")
    print(doc.page_content)
    print("-" * 50)