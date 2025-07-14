import chromadb
from chromadb.config import Settings


client = chromadb.PersistentClient(path="./chroma_storage", settings=Settings(anonymized_telemetry=True))

collection = client.get_or_create_collection("events_snowflake-arctic-embed2", metadata={
    "hnsw:space": "cosine",
    "hnsw:construction_ef": 256,
    "hnsw:M": 48,
    "hnsw:search_ef": 64
})




def save_event_vector(event_id, event_description, vector):
    collection.add(
        ids=[str(event_id)],
        documents=[event_description],
        embeddings=[vector]
    )
    print(f"added vector {event_id}")
     


def delete_event_vector(event_id):
    collection.delete(
        ids=[str(event_id)]
    )
    print(f"Видалення вектора з ID: {event_id}")