from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def get_embeddings(chunks):
    embeddings= OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore

def create_conversation(vectorstore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversastion_chain = ConversationalRetrievalChain.from_llm(
       llm=llm,
       retriever=vectorstore.as_retriever(),
       memory=memory
   )
    return conversastion_chain