from langchain.chains import RetrievalQA
from langchain.chat_models import ChatGoogleGenerativeAI
from langchain.vectorstores import FAISS

def load_faiss(user_id, doc_id, admin=False):
    if admin:
        # Load all stores or loop through them
        return FAISS.load_local(f"data/vector_store/all_combined", embeddings)
    return FAISS.load_local(f"data/vector_store/{user_id}_{doc_id}", embeddings)

def query_doc(question, retriever):
    model = ChatGoogleGenerativeAI(model="gemini-pro")
    qa = RetrievalQA.from_chain_type(llm=model, retriever=retriever.as_retriever())
    return qa.run(question)
