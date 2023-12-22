
# EmbeddingGenerator.py
import csv
from openai import OpenAI
import os


client = OpenAI(api_key='YourKey')

def generate_embedding(text):
    try:
        response = client.embeddings.create(
            model="text-embedding-ada-002", 
            input=text
        )
        #print("Embedding response:", response)  # Print the response object
        # You might need to adjust the next line based on the response structure
        return response.data[0].embedding
    except Exception as e:
        print(f"Error generating embedding: {e}")
        return None


def log_embedding(uuid, embedding):
    embeddings_file_path = os.path.join("data", "embeddings", "embeddings_log.csv")
    with open(embeddings_file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([uuid, *embedding])

def initialize_embeddings_file():
    # Directory where the embeddings file will be stored
    embeddings_dir = os.path.join("data", "embeddings")
    embeddings_file_path = os.path.join(embeddings_dir, "embeddings_log.csv")

    # Create the embeddings directory if it does not exist
    if not os.path.exists(embeddings_dir):
        os.makedirs(embeddings_dir)

    # Create the embeddings file with headers if it does not exist
    if not os.path.isfile(embeddings_file_path):
        with open(embeddings_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['UUID', 'Embedding'])