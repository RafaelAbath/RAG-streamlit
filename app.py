import streamlit as st
from utils import split, embbedings
from dotenv import load_dotenv
from streamlit_chat import message
import os


load_dotenv()


def main():
    st.set_page_config(
        page_title="RAG Com Streamlit")
    st.title("RAG Chatbot")
    st.write("O RAG Chatbot é um chatbot que utiliza os seus documentos para responder perguntas.")
    
    st.header("Converse com o RAG Chatbot")
    user_questions = st.text_input("Digite sua pergunta")
    
    
    if "conversation" not in st.session_state:
        st.session_state.conversation = None


    if user_questions and st.session_state.conversation:
        response = st.session_state.conversation(user_questions)['chat_history'][-1]
        message(user_questions, is_user=True)
        message(response.content, is_user=False)

        st.write(response.content)

    with st.sidebar:
        st.subheader("Seus arquivos")
        pdf_loader = st.file_uploader("Carregar PDF", type=["pdf"], accept_multiple_files=True)
       
        if st.button("Processar"):
          
            processados = split.process_files(pdf_loader)
            chunks = split.split_text_chunks(processados)
            vectorstore = embbedings.get_embeddings(chunks)
            st.write("Processado com sucesso")
            
          
            st.session_state.conversation = embbedings.create_conversation(vectorstore)


if __name__ == "__main__":
    main()
