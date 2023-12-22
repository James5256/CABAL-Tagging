
# ContextWindowManager.py
import csv
import os

def read_conversation_log():
    conversation_log = {}
    conversation_log_file_path = os.path.join("data", "logs", "conversation_log.csv")

    with open(conversation_log_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            uuid, conv_id, _, user_input, chatbot_response = row  # Adjusted to include conv_id
            conversation_log[uuid] = (conv_id, user_input, chatbot_response)  # Store conv_id as well
    return conversation_log

def form_context_window(relevant_uuids, max_tokens=500):
    conversation_log = read_conversation_log()
    context = ""
    total_tokens = 0

    for uuid in relevant_uuids:
        entry = conversation_log.get(uuid, None)
        if entry is not None:
            _, user_input, chatbot_response = entry  # Adjusted to include conv_id

            segment = f"User: {user_input}\nChatbot: {chatbot_response}\n"

            segment_tokens = len(segment.split())
            if total_tokens + segment_tokens <= max_tokens:
                context += segment
                total_tokens += segment_tokens
            else:
                break  # Stop adding segments if token limit is reached

    return context

def get_specific_context(uuid):
    conversation_log = read_conversation_log()
    if uuid in conversation_log:
        _, user_input, chatbot_response = conversation_log[uuid]  # Corrected unpacking
        return [{"role": "user", "content": user_input}, {"role": "assistant", "content": chatbot_response}]
    return []
