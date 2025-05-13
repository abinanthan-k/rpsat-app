import streamlit as st
from utils.auth import login
from utils.pdf_parser import extract_text_from_pdf
from utils.chunk import chunk_text
from utils.vector_store import embed_and_store
from utils.summarizer import summarize
from utils.rag import load_faiss, query_doc

if "user" not in st.session_state:
    if not login():
        st.stop()

st.title("📄 Research Insight Engine")

role = st.session_state["role"]
user = st.session_state["user"]

uploaded_file = st.file_uploader("Upload your research paper", type="pdf")

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    st.write("✅ Extracted text.")
    chunks = chunk_text(text)
    doc_id = uploaded_file.name
    embed_and_store(chunks, user, doc_id)
    st.success("Chunks embedded and stored successfully.")
    
    if st.button("Summarize Paper"):
        summary = summarize(text)
        st.subheader("📌 Summary")
        st.write(summary)

if st.text_input("Ask a question from your documents"):
    retriever = load_faiss(user, doc_id, admin=(role=="admin"))
    answer = query_doc(st.session_state.get("question"), retriever)
    st.write("💬 Answer:", answer)
