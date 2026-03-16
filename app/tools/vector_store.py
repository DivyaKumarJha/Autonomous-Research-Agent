from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.memory import state

embedding = OllamaEmbeddings(
    model="nomic-embed-text"
)

vector_db = Chroma(
    collection_name="research_docs",
    embedding_function=embedding,
    persist_directory="./chroma_db"
)


def store_documents(documents):

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=200
    )

    all_chunks = []
    metadata = []

    for doc in documents:

        url = doc["url"]
        text = doc["text"]

        chunks = splitter.split_text(text)

        for chunk in chunks:

            all_chunks.append(chunk)

            metadata.append({
                "url": url,
                "source": "web"
            })

    if len(all_chunks) > 0:

        vector_db.add_texts(
            texts=all_chunks,
            metadatas=metadata
        )
        
def search_documents(query, k=5):

    docs = vector_db.similarity_search(query, k=k, filter={"source": "web"})

    return docs    