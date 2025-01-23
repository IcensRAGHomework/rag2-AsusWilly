from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    documents = loader.load()
    splitter = CharacterTextSplitter(chunk_overlap = 0)
    chunks = splitter.split_documents(documents)
    return chunks[-1]

def hw02_2(q2_pdf):
    pass

print(hw02_1(q1_pdf))
# hw02_1(q2_pdf)