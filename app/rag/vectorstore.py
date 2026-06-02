from langchain_community.vectorstores import Chroma
from app.config.settings import CHROMA_PATH


def create_vectorstore(chunks, embedding_model):

    vectorstore = Chroma.from_texts(
        texts=chunks, embedding=embedding_model, persist_directory=CHROMA_PATH
    )

    return vectorstore
