
# RelevanceAssessment.py
import ContextWindowManager
import numpy as np
import csv
import os

def cosine_similarity(v1, v2):
    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))

def read_embeddings():
    embeddings_file_path = os.path.join("data", "embeddings", "embeddings_log.csv")
    embeddings = {}

    with open(embeddings_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            uuid = row[0]
            embedding = np.array(row[1:], dtype=float)
            embeddings[uuid] = embedding
    return embeddings


def find_relevant_interactions(new_input_embedding):
    embeddings = read_embeddings()
    relevance_scores = {}

    for uuid, embedding in embeddings.items():
        similarity = cosine_similarity(new_input_embedding, embedding)
        relevance_scores[uuid] = similarity

    sorted_uuids = sorted(relevance_scores, key=relevance_scores.get, reverse=True)
    return sorted_uuids[:5]  # Return only the top 5 UUIDs


def find_top_five_interactions(query_embedding, current_query, threshold=0.7):
    embeddings = read_embeddings()
    conversation_log = ContextWindowManager.read_conversation_log()
    top_five = []  # This will store tuples of (similarity, uuid)

    for uuid, embedding in embeddings.items():
        _, past_user_input, _ = conversation_log.get(uuid, (None, "", None))


        # Skip entries with identical or empty content
        if past_user_input.strip().lower() == current_query.strip().lower() or not past_user_input:
            continue

        similarity = cosine_similarity(query_embedding, embedding)

        if similarity > threshold:
            top_five.append((similarity, uuid))
            top_five = sorted(top_five, key=lambda x: x[0], reverse=True)[:5]

    return [uuid for _, uuid in top_five]  # Return only the UUIDs