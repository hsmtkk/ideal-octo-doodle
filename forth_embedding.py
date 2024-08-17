import os
import os.path
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import BSHTMLLoader


docs = list()
for name in os.listdir("chapters"):
    path = os.path.join("chapters", name)
    loader = BSHTMLLoader(path, open_encoding="utf-8")
    doc = loader.load()
    docs.extend(doc)
print(docs)

embeddings = OpenAIEmbeddings()

faiss = FAISS.from_documents(docs, embeddings)
faiss.save_local("faiss")
