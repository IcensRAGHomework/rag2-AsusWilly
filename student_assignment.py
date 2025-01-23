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
    full_text = " ".join([doc.page_content for doc in documents])
    pattern = r'(第[一二三四五六七八九十百千]+[章條])'
    sections = re.split(pattern, full_text)
    chunks = []
    for i in range(1, len(sections), 2): 
        title = sections[i]
        content = sections[i + 1] if i + 1 < len(sections) else ''
        full_chunk = title + content
        chunks.append(full_chunk)

    final_chunks = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_overlap=0)
    for chunk in chunks:
        split_chunks = text_splitter.split_text(chunk)
        final_chunks.extend(split_chunks)
    return len(chunks)

# print(hw02_1(q1_pdf))
# print(hw02_2(q2_pdf))