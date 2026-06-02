from langchain_openai import OpenAIEmbeddings
from app.config.settings import EMBEDDING_MODEL


def get_embedding_model():

    return OpenAIEmbeddings(model=EMBEDDING_MODEL)
