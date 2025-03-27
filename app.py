import streamlit as st
from utils import split, embbedings
from dotenv import load_dotenv
import os

# Carregar variáveis do arquivo .env
load_dotenv()


def main():
    st.set_page_config(
        page_title="RAG Com Streamlit")
    st.title("RAG Chatbot")
    st.write("O RAG Chatbot é um chatbot que utiliza os seus documentos para responder perguntas.")
    
    
    with st.sidebar:
        st.subheader("seus arquivos")
        pdf_loader = st.file_uploader("Carregar PDF", type=["pdf"], accept_multiple_files=True)
       
        if st.button("Processar"):
            processados = split.process_files(pdf_loader)
           
            chunks = split.split_text_chunks(processados)
            vectorstore = embbedings.get_embeddings(chunks)
            st.write("Processado com sucesso")

if __name__ == "__main__":
    main()