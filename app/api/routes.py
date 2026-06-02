from fastapi import APIRouter

from app.rag.loader import load_youtube_transcript
from app.rag.chunking import split_text
from app.rag.embeddings import get_embedding_model
from app.rag.vectorstore import create_vectorstore
from app.rag.retriever import create_retriever
from app.rag.chain import build_rag_chain

router = APIRouter()

qa_chain = None


@router.post("/load-video")
def load_video(video_id: str):

    global qa_chain

    text = load_youtube_transcript(video_id)

    chunks = split_text(text)

    embedding_model = get_embedding_model()

    vectorstore = create_vectorstore(chunks, embedding_model)

    retriever = create_retriever(vectorstore)

    qa_chain = build_rag_chain(retriever)

    return {"message": "Video loaded successfully"}


@router.post("/ask")
def ask_question(question: str):

    global qa_chain

    if qa_chain is None:
        return {"error": "Load a video first"}

    answer = qa_chain.invoke(question)  # ← pass string directly

    return {"answer": answer}
