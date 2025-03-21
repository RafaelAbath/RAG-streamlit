import streamlit as st
from utils import files

def main():
    st.title("RAG Chatbot")
    st.write("O RAG Chatbot é um chatbot que utiliza os seus documentos para responder perguntas.")
    
    
    with st.sidebar:
        st.subheader("seus arquivosr")
        pdf_loader = st.file_uploader("Carregar PDF", type=["pdf"], accept_multiple_files=True)
        print(pdf_loader)
        if st.button("Processar"):
            processar = files.process_files(pdf_loader)
            print(processar)
        
if __name__ == "__main__":
    main()