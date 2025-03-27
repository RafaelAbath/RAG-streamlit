from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS

def get_embeddings(chunks):
    embeddings= OpenAIEmbeddings()
    vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    return vectorstore