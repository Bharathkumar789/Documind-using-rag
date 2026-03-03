import streamlit as st
from document_processor import load_pdf, split_text
from vector_store import VectorStore
from qa_engine import generate_answer

st.title("📄 DocuMind – Document QA System")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if "vector_store" not in st.session_state:
    st.session_state.vector_store = VectorStore()

if uploaded_file:

    with st.spinner("Processing document..."):
        text = load_pdf(uploaded_file)
        chunks = split_text(text)
        st.session_state.vector_store.create_index(chunks)

    st.success("Document processed successfully!")

    question = st.text_input("Ask a question about the document")

    if question:
        retrieved_chunks = st.session_state.vector_store.search(question)
        answer = generate_answer(retrieved_chunks, question)

        st.subheader("Answer:")
        st.write(answer)

        st.subheader("Retrieved Context:")
        for chunk in retrieved_chunks:
            st.write(chunk[:300] + "...")