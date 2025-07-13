import chromadb
from chromadb.config import Settings


client = chromadb.PersistentClient(path="/Users/ilapetuhov/Test Task From dear Illia Petukhov for dear company Join.To.IT/chroma_storage", settings=Settings(anonymized_telemetry=True))
collection = client.get_or_create_collection("events")




def save_event_vector(event_id, event_description, vector):
    collection.add(
        ids=[str(event_id)],
        documents=[event_description],
        embeddings=[vector]
    )
    print(f"Event {event_id} added to Chroma.")
    

def delete_event_vector(event_id):
    collection.delete(
        ids=[str(event_id)]
    )
    print(f"Видалення вектора з ID: {event_id}")