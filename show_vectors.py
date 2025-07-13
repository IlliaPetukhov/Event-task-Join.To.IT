import chromadb
from chromadb.config import Settings
from Event.generate_vector import generate_embedding



client = chromadb.PersistentClient(path="/Users/ilapetuhov/Test Task From dear Illia Petukhov for dear company Join.To.IT/chroma_storage", settings=Settings(anonymized_telemetry=True))
collection = client.get_or_create_collection("events")

all_data = collection.get(include=[])
print(all_data)
# query_vector = generate_embedding("Я шукаю подію зі смачною вуличною їжею, де будуть шеф-кухарі, дегустації та музика.")
# results = collection.query(
#     query_embeddings=[query_vector],
#     n_results=2,
#     include=["documents", "distances"]
# )
# print(results)