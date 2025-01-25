import re
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
    loader = PyPDFLoader(q2_pdf)
    documents = loader.load()
    full_text = '\f'.join([doc.page_content for doc in documents])
    pattern = [r'第\s+[一二三四五六七八九十]+\s+章', r'第\s[\d-]+\s+條']
    chunks = RecursiveCharacterTextSplitter(
        separators = pattern,
        chunk_overlap = 0,
        chunk_size = 1,
        is_separator_regex = True,
        keep_separator = True).split_text(full_text)
    return len(chunks)

# print(hw02_1(q1_pdf))
print(hw02_2(q2_pdf))