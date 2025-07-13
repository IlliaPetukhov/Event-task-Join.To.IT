import ollama


def generate_embedding(text):
    response = ollama.embeddings(
        model='mxbai-embed-large',
        prompt=text
    )
    embedding = response.embedding
    return embedding
   

