from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_overlap = 0)
    for i, doc in enumerate(documents):
        page_number = i + 1
        chunks = splitter.split_text(doc.page_content)
        for j, chunk in enumerate(chunks):
            last_chunk_info = {
                'filename': q1_pdf,
                'page': page_number,
                'content': chunk
            }
    return last_chunk_info

def hw02_2(q2_pdf):
    pass

hw02_1(q1_pdf)
# hw02_1(q2_pdf)