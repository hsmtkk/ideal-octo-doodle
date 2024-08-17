import os
import os.path
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import BSHTMLLoader
from langchain_core.documents.base import Document


def load_docs() -> list[Document]:
    docs = list()
    for name in os.listdir("chapters"):
        path = os.path.join("chapters", name)
        loader = BSHTMLLoader(path, open_encoding="utf-8")
        doc = loader.load()
        docs.extend(doc)
    return docs


if __name__ == "__main__":
    docs = load_docs()
    print(docs)

    embeddings = OpenAIEmbeddings()

    faiss = FAISS.from_documents(docs, embeddings)
    faiss.save_local("faiss")
