from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
import os

def embed_and_store(chunks, user_id, doc_id):
    embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_texts(
        texts=chunks,
        embedding=embedding,
        metadatas=[{"user": user_id, "doc": doc_id}] * len(chunks)
    )
    save_path = f"data/vector_store/{user_id}_{doc_id}"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    vectorstore.save_local(save_path)
