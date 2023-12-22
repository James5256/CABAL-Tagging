    
# ChatbotInterface.py
from openai import OpenAI

client = OpenAI(api_key='YourKey')

def get_chatbot_response(user_input, combined_context):
    try:
        messages = [{"role": "system", "content": "You are a helpful assistant."}]
        messages += combined_context
        messages.append({"role": "user", "content": user_input})

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error: {e}")
        return "I am unable to respond at this time."
