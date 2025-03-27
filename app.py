import streamlit as st
from utils import split, embbedings
from dotenv import load_dotenv
from streamlit_chat import message
import os

# Carregar variáveis do arquivo .env
load_dotenv()

# Carregar o arquivo CSS com o estilo do tema escuro
def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Configurar a página e tema
st.set_page_config(page_title="RAG Com Streamlit", layout="wide")
load_css()  # Carregar o estilo CSS

def main():
    st.title("RAG Chatbot")
    st.write("O RAG Chatbot é um chatbot que utiliza os seus documentos para responder perguntas.")
    
    # Seção para o usuário interagir
    st.header("Converse com o RAG Chatbot")
    user_questions = st.text_input("Digite sua pergunta")
    
    # Inicializar a conversa, se necessário
    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    # Se o usuário fez uma pergunta e já existe uma conversa ativa
    if user_questions and st.session_state.conversation:
        response = st.session_state.conversation(user_questions)['chat_history'][-1]
        message(user_questions, is_user=True)
        message(response.content, is_user=False)
        st.write(response.content)

    # Sidebar para upload de arquivos PDF
    with st.sidebar:
        st.subheader("Seus arquivos")
        pdf_loader = st.file_uploader("Carregar PDF", type=["pdf"], accept_multiple_files=True)

        if st.button("Processar"):
            if pdf_loader:
                processados = split.process_files(pdf_loader)
                chunks = split.split_text_chunks(processados)
                vectorstore = embbedings.get_embeddings(chunks)
                st.write("Processado com sucesso")
                # Criar a conversa com base no vetor gerado
                st.session_state.conversation = embbedings.create_conversation(vectorstore)
            else:
                st.warning("Por favor, faça o upload de um arquivo PDF antes de processar.")

if __name__ == "__main__":
    main()
