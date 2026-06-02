from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

CHROMA_PATH = "chroma_db"

MODEL_NAME = "gpt-4o-mini"

EMBEDDING_MODEL = "text-embedding-3-small"