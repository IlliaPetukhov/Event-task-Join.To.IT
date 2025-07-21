from chromadb import PersistentClient
from chromadb.config import Settings

client = PersistentClient(
    path="./chroma_storage",
    settings=Settings(anonymized_telemetry=True)
)

collection = client.get_or_create_collection(
    "events_snowflake-arctic-embed2",
    metadata={
        "hnsw:space": "cosine",
        "hnsw:construction_ef": 256,
        "hnsw:M": 48,
        "hnsw:search_ef": 64
    }
)