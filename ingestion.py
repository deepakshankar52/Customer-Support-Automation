from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

# from embeddings import LocalEmbeddings
from embeddings import get_embedding_model


loader = PyPDFDirectoryLoader("knowledge_base")

documents = loader.load()

print(f"Loaded {len(documents)} pages")


splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=150
)

chunks = splitter.split_documents(documents)

print(f"Created {len(chunks)} chunks")


# embedding_model = LocalEmbeddings()
embedding_model = get_embedding_model()

vector_db = FAISS.from_documents(
    chunks,
    embedding_model
)

vector_db.save_local("vector_store")

print("Vector database created successfully.")