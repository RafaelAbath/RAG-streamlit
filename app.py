import streamlit as st
from PyPDF2 import PdfReader

def main():
    st.title("RAG Chatbot")
    st.write("O RAG Chatbot é um chatbot que utiliza os seus documentos para responder perguntas.")
    
    
    with st.sidebar:
        st.subheader("seus arquivosr")
        pdf_loader = st.file_uploader("Carregar PDF", type=["pdf"], accept_multiple_files=True)
        print(pdf_loader)
        if st.button("carregar"):
            pass
    
        
if __name__ == "__main__":
    main()