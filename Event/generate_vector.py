import ollama


def generate_embedding(text):
    response = ollama.embeddings(
        model="snowflake-arctic-embed2:latest",
        prompt=text
    )
    embedding = response.embedding
    return embedding


#print(generate_embedding("Привіт як ти"))
   

