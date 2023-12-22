
import ChatbotInterface
import ConversationLogger
import EmbeddingGenerator
import RelevanceAssessment
import ContextWindowManager

def main():
    # Initialize log files
    EmbeddingGenerator.initialize_embeddings_file()
    ConversationLogger.initialize_conversation_log_file()

    print("Chatbot Interface Initialized.")
    KEYWORD = "recallz"
    RESET_KEYWORD = "reset_context"  # Define the reset keyword
    ongoing_context = []  # Initialize an empty context list
    is_first_input = True  # Flag to check if it's the first user input
    conversation_id = ConversationLogger.start_new_conversation()

    while True:
        user_input = input("You: ")

        # Check for exit command
        if user_input.lower() == 'exit':
            # End the current conversation
            ConversationLogger.end_conversation(conversation_id)
            break

        # Check for reset command
        if user_input.lower() == RESET_KEYWORD:
            ongoing_context = []  # Reset the ongoing context
            print("Context has been reset.")
            continue  # Skip the rest of the loop

        # Process the UUID command at the beginning of a conversation
        if is_first_input and user_input.lower().startswith("uuid:"):
            uuids = user_input[5:].strip().split()  # Assuming UUIDs are space-separated
            for uuid in uuids:
                try:
                    summary = ConversationLogger.get_conversation_summary(uuid)
                    ongoing_context.append({"role": "system", "content": f"Summary of conversation {uuid}: {summary}"})
                except Exception as e:
                    print(f"Error retrieving summary for conversation {uuid}: {e}")
            is_first_input = False
            continue

        # Generate embedding for the current user input
        current_input_embedding = EmbeddingGenerator.generate_embedding(user_input)
        # Find relevant past interactions
        relevant_uuids = RelevanceAssessment.find_relevant_interactions(current_input_embedding)

        context_strs = []
        for uuid in relevant_uuids:
            # Form the context window for each relevant UUID
            context_str = ContextWindowManager.form_context_window([uuid], max_tokens=500)
            context_strs.append(context_str)

        # Combine all context windows
        combined_context_str = "\n".join(context_strs)

        # Convert the combined context string into a list of dictionaries
        historical_context = []
        for line in combined_context_str.split('\n'):
            if line.startswith("User: "):
                historical_context.append({"role": "user", "content": line[6:]})
            elif line.startswith("Chatbot: "):
                historical_context.append({"role": "assistant", "content": line[9:]})

        # Check for the keyword and perform a specific search
        combined_context = ongoing_context + historical_context
        if KEYWORD in user_input.lower():
            # Extract the query from the user input
            query = user_input.replace(KEYWORD, "").strip()
            print("Query for recall:", query)  # Debugging print statement
            query_embedding = EmbeddingGenerator.generate_embedding(query)
            relevant_uuids = RelevanceAssessment.find_top_five_interactions(query_embedding, query)
            print("Relevant UUIDs:", relevant_uuids)  # Debugging print statement

            specific_contexts = []
            for uuid in relevant_uuids:
                # Fetch the specific past interaction for each UUID
                specific_context = ContextWindowManager.get_specific_context(uuid)
                specific_contexts.extend(specific_context)  # Extend instead of append

            combined_context = ongoing_context + specific_contexts
        else:
            # Normal context combination
            combined_context = ongoing_context + historical_context

        # Print the combined context for debugging
        #print("Combined Context:", combined_context)

        # Generate chatbot response considering both the ongoing context and the historical context
        chatbot_response = ChatbotInterface.get_chatbot_response(user_input, combined_context)
        print(f"Chatbot: {chatbot_response}")

        # Update ongoing context
        ongoing_context.append({"role": "user", "content": user_input})
        ongoing_context.append({"role": "assistant", "content": chatbot_response})


        # Log the interaction
        interaction_uuid = ConversationLogger.log_interaction(conversation_id, user_input, chatbot_response)
        user_embedding = EmbeddingGenerator.generate_embedding(user_input)
        if user_embedding is not None:
            EmbeddingGenerator.log_embedding(interaction_uuid, user_embedding)
        bot_embedding = EmbeddingGenerator.generate_embedding(chatbot_response)
        if bot_embedding is not None:
            EmbeddingGenerator.log_embedding(interaction_uuid, bot_embedding)

if __name__ == "__main__":
    main()