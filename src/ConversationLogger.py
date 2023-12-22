
# ConversationLogger.py
import csv
import uuid
import os
from datetime import datetime
from openai import OpenAIError, OpenAI

def initialize_conversation_log_file():
    conversation_log_dir = os.path.join("data", "logs")
    conversation_log_file_path = os.path.join(conversation_log_dir, "conversation_log.csv")

    if not os.path.exists(conversation_log_dir):
        os.makedirs(conversation_log_dir)

    if not os.path.isfile(conversation_log_file_path):
        with open(conversation_log_file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Update the headers to include 'ConvID'
            writer.writerow(['UUID', 'ConvID', 'Timestamp', 'UserInput', 'ChatbotResponse'])


def start_new_conversation():
    conv_id = str(uuid.uuid4())
    log_conversation_stamp(conv_id, "Start")
    return conv_id


def end_conversation(conv_id):
    # Generate a summary for the conversation
    conversation_summary = summarize_conversation(conv_id)

    # Log the summary before marking the conversation as ended
    log_conversation_entry(conv_id, "Summary", conversation_summary)

    # Mark the conversation as ended
    log_conversation_stamp(conv_id, "End")

def log_conversation_entry(conv_id, entry_type, content):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation_log_file_path = os.path.join("data", "logs", "conversation_log.csv")

    with open(conversation_log_file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Use conv_id as the UUID for the summary entry
        writer.writerow([conv_id, conv_id, timestamp, entry_type, content])

def log_conversation_stamp(conv_id, stamp_type):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation_log_file_path = os.path.join("data", "logs", "conversation_log.csv")

    with open(conversation_log_file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # The line below should log the stamp information, not the header row
        writer.writerow([str(uuid.uuid4()), conv_id, timestamp, stamp_type, "System"])

def log_interaction(conv_id, user_input, chatbot_response):
    interaction_uuid = str(uuid.uuid4())
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conversation_log_file_path = os.path.join("data", "logs", "conversation_log.csv")

    with open(conversation_log_file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Now the function writes the conv_id as well
        writer.writerow([interaction_uuid, conv_id, timestamp, user_input, chatbot_response])

    return interaction_uuid


client = OpenAI(api_key='YourKey')
def summarize_conversation(conv_id, model="gpt-4"):
    conversation_log_file_path = os.path.join("data", "logs", "conversation_log.csv")
    conversation_text = ""
    conversation_started = False

    with open(conversation_log_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == conv_id:  # Use ConvID here
                if row[3] == "Start":
                    conversation_started = True
                    continue
                elif row[3] == "End" or row[3] == "Summary":
                    break
                if conversation_started:
                    user_input, chatbot_response = row[3], row[4]
                    conversation_text += f"User: {user_input}\nChatbot: {chatbot_response}\n"
    
    # Using OpenAI's GPT model for summarization
    system_message = "Summarize the following conversation in detail, highlighting key interactions and the overall topic. The summarization should allow refernce to the details of the conversation from which the summary was obtained within a new conversation that would otherwise not have access to this information:"
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "system", "content": system_message},
                      {"role": "user", "content": conversation_text}]
        )
        return response.choices[0].message.content.strip()
    except OpenAIError as e:
        print("An OpenAIError occurred:", e)
        raise
    except Exception as e:
        print("An unexpected error occurred:", e)
        raise



def get_conversation_summary(conv_id):
    conversation_log_file_path = os.path.join("data", "logs", "conversation_log.csv")
    summary = ""

    with open(conversation_log_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[1] == conv_id and row[3] == "Summary":
                summary = row[4]
                break  # Assuming there's only one summary per conversation

    return summary
