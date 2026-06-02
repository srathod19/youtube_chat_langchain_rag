from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from app.config.settings import MODEL_NAME


def build_rag_chain(retriever):
    llm = ChatOpenAI(model=MODEL_NAME, temperature=0)

    prompt = ChatPromptTemplate.from_template("""
        Answer the user's question using only the context below.

        Context:
        {context}

        Question:
        {input}
        """)

    def format_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    chain = (
        {"context": retriever | format_docs, "input": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain
