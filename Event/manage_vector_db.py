from chroma_client import collection


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