from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_overlap = 0)
    for i, doc in enumerate(documents):
        chunks = splitter.split_text(doc.page_content)
        for j, chunk in enumerate(chunks):
            last_chunk_info = chunk
    return last_chunk_info

def hw02_2(q2_pdf):
    pass

print(hw02_1(q1_pdf))
# hw02_1(q2_pdf)