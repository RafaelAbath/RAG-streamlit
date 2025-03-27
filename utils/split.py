from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
def process_files(files):
    
    text = ""
    for file in files:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
def split_text_chunks(text):
    chunks_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1500,
        chunk_overlap=300,
        length_function=len,
    )
    chunks = chunks_splitter.split(text)
    return chunks