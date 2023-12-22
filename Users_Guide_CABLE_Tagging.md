
# Users Guide CABAL-Tagging

## Introduction
This tutorial covers the functionality of a chatbot program designed to interact with users, maintain conversation context, and recall past interactions. The program utilizes modules like ChatbotInterface, ConversationLogger, EmbeddingGenerator, RelevanceAssessment, and ContextWindowManager.

## Modules Overview
- **ChatbotInterface.py**: Manages interactions with the OpenAI API for generating chatbot responses.
- **ConversationLogger.py**: Logs conversations, providing functionality for starting, ending, and summarizing conversations.
- **EmbeddingGenerator.py**: Generates embeddings for user inputs and responses for relevance assessment.
- **RelevanceAssessment.py**: Evaluates the relevance of past interactions based on embeddings.
- **ContextWindowManager.py**: Manages the context window for conversations, enabling the bot to refer to previous interactions.

## Key Features
- **Context Management**: Maintains an ongoing conversation context.
- **Dynamic Recall**: Uses past interactions to inform current responses.
- **Conversation Logging**: Logs interactions for reference and analysis.

## Usage Example
### Starting a Conversation
When a user starts a conversation, the bot initializes and is ready to accept inputs.

**User**: "Hi, Assistant! I want to create a story with two characters..."

### Handling Specific Requests
The bot can handle specific requests such as naming characters or describing settings.

**Chatbot**: "Of course! Let's start by giving the first character a name..."

### Recalling Past Interactions
The `recallz` keyword triggers the bot to recall relevant past interactions. For example:

**User**: "recallz Can you please tell me the description given regarding the land the story takes place in?"

The bot recalls and provides the requested information.

Note! This function is not required if the context window still contains the information desired for recall.

### Resetting Context
The `reset_context` command clears the ongoing conversation context.

**User**: "reset_context"

The 'recallz' function is especially useful if the current context window is reset.

### Exiting the Conversation
To exit the conversation, the user simply types "exit".

**User**: "exit"

When the program is exited, a summary of the conversation will be recorded in the conversation logs.

To recall the converastion summary, extract the UUID associated with the conversation from the conversation logs. 
Next, in the chat input, type, uuid: followed by the approprate UUID from the log.

Note! Each input/output combination are assigned a UUID and a conversation UUID.
The input/output specific UUIDs can be used to recall the associated context only. 
This can be useful if some require detail is not included with the conversation summary method.

## Limitations and Examples
### Inconsistencies in Recall
The bot may show limitations in recalling specific details accurately. For example:

**User**: "What was Jane's eye color described as earlier?"
**Chatbot**: "I apologize for the confusion. Earlier, Jane's eye color was not mentioned..."

This highlights a limitation where the bot fails to recall specific attributes that were indeed mentioned earlier.
However, this limitation can be overcome by implimenting specific UUID calls, as described above.

### Potential Solutions
- **Improved Context Management**: Enhance the context window management to capture and recall details more effectively.
- **Advanced Relevance Algorithms**: Implement more sophisticated algorithms for determining the relevance of past interactions.
- **User Input Validation**: Introduce mechanisms to validate user inputs for consistency.

## Conclusion
This tutorial provides an overview of the chatbot program, showcasing its capabilities and limitations. While the program effectively manages conversations and recalls past interactions, it has areas for improvement in terms of recall accuracy and detail handling.
Although this code is intended to improve the context window of OpenAI's ChatGPT 3.5, it is possible to adapt the program to function with open-source models.
However, I have been limited to ChatGPTs API due to personal compute limitations.



## Following is the conversation example, with the chatbot, that is referneced throughout this document.
Chatbot Interface Initialized.
You: Hi, Assistant! I want to create a story with two characters. The characters do something that causes something to happen. Can we start by giving the characters' names and genders? 
Chatbot: Of course! Let's start by giving the first character a name and gender. What would you like the first character's name and gender to be?
You: Can we call the first character, Jane, who is female?
Chatbot: Certainly! We'll call the first character Jane, a female. And what about the second character? What name and gender do you have in mind for them?
You: Let's call the second character, Jake, who is male.
Chatbot: Great! So we have Jane as our first character, who is female, and Jake as our second character, who is male. Now that we have our characters, let's think about what they could do that would cause something to happen. Is there a particular setting or scenario you have in mind for the story?
You: We will get to the story soon! However, can we first come up with descriptions for the two characters?
Chatbot: Of course! Let's start by describing Jane, our female character. How would you like to describe her?
You: Can you please provide me with descriptions for both characters?
Chatbot: Of course, I can help you with that! Here are descriptions for Jane and Jake:

Jane:
Jane is a young woman in her late twenties. She has long, flowing brown hair that frames her face beautifully. Her bright blue eyes are full of curiosity, and her warm smile is always ready to greet others. Jane has a slender figure and carries herself with confidence. She is known for her kind and compassionate nature, always willing to lend a helping hand to those in need. Jane has a passion for art and can often be seen creating beautiful paintings or sculptures in her free time.

Jake:
Jake is a tall and athletic man in his early thirties. He has short, wavy brown hair and a charming smile that can easily win people over. His hazel eyes sparkle with intelligence and determination. Jake has a muscular build, hinting at his dedication to fitness and an active lifestyle. He is adventurous and loves exploring the outdoors, often participating in various sports and activities. Jake has a knack for mechanics and can fix just about anything, which has earned him a reputation as the neighborhood handyman.

I hope these descriptions bring our characters to life for you! Let me know if there's anything else I can assist you with.
You: These are excellent! Thank you so much! Can we move on to the first paragraph of the story? This paragraph should introduce the world of the story! The two characters should not be mentioned in this paragraph!
Chatbot: Certainly! Here's the first paragraph introducing the world of the story without mentioning the characters:

"In a world where technology reigns supreme, towering skyscrapers scrape the heavens while bustling crowds fill the streets below. Neon lights illuminate the cityscape, casting an otherworldly glow on the sidewalks. The hum of futuristic vehicles permeates the air as they zip by, their sleek designs reflecting the cutting-edge advancements of this metropolis. It is a place where possibilities seem endless, and dreams are woven into the very fabric of reality. Welcome to a world where innovation and progress converge, creating a captivating backdrop for our tale to unfold."
You: Oh, thank you so much for this great paragraph! Can we move on to the second paragraph? The second paragraph should introduce the characters in a creative way, incorporating the descriptions of the characters we decided on earlier!
Chatbot: Certainly! Here's the second paragraph, incorporating the descriptions of the characters we decided on earlier:

"In this vast and vibrant city, amidst the towering structures and pulsing energy, two individuals stand at the cusp of their destinies. Jane, a young woman with long, flowing brown hair that catches the sunlight, navigates the streets with an air of grace and compassion. Her bright blue eyes mirror her boundless curiosity, reflecting a world she yearns to explore. She carries herself with confidence, a gentle smile always present on her lips, as she goes about her day, her heart brimming with artistic passion. On another corner of the metropolis, Jake, a tall and athletic man with wavy brown hair, moves with purpose and charm. His hazel eyes, shining with intelligence, gaze at the world with an unrelenting determination to leave his mark. Among the crowd, his muscular frame suggests an active lifestyle, and his hands, adept in mechanics, carry the capability to mend the broken. In this remarkable city, Jane and Jake are but two stars about to collide, each holding within them the power to shape this vivid tapestry of life."

I hope this paragraph effectively introduces the characters in a creative way, highlighting their unique qualities! Let me know if there's anything else I can assist you with.
You: Can we move on to the third paragraph? Can you please make this paragraph about our two characters being faced with some sort of challenge that tests their resilience and skills?
Chatbot: Certainly! Here's the third paragraph, featuring our two characters facing a challenge that tests their resilience and skills:

"Little did Jane and Jake know that destiny had a challenge in store for them, a test that would push their resilience and skills to the limit. One fateful day, an unprecedented storm descended upon the city, unleashing chaos in its wake. Violent winds buffeted the buildings, and rain poured down relentlessly, flooding the streets. With power outages and communication lines faltering, the city found itself in a state of disarray. Despite the chaos, Jane and Jake refused to succumb to despair. Drawing upon their individual talents and unwavering determination, they vowed to help those in need, navigating the treacherous conditions and lending a hand wherever they could. Together, they faced the storm head-on, their unwavering spirit guiding them through the tempest as they emerged as beacons of hope in the darkness."

I hope this paragraph captures the challenge our characters face and highlights their resilience and skills. Let me know if there's anything else I can assist you with!
You: reset_context
Context has been reset.
You: recallz Can you please tell me the description given regarding the land the story takes place in?
Query for recall: Can you please tell me the description given regarding the land the story takes place in?
Relevant UUIDs: ['473f9ab0-8c77-4e24-a788-9ae4be81e245', '6f683b3a-ea88-4513-a350-c898f0362bf0', '161a7a8c-3bd7-4e88-a020-f96929c4ba2e', '04bd77db-389f-45a6-a9b8-4822513d97fb', '328de796-c06e-4cb6-a559-00405602cf21']
Chatbot: Certainly! The description given for the land where the story takes place is as follows:

"In a world where technology reigns supreme, towering skyscrapers scrape the heavens while bustling crowds fill the streets below. Neon lights illuminate the cityscape, casting an otherworldly glow on the sidewalks. The hum of futuristic vehicles permeates the air as they zip by, their sleek designs reflecting the cutting-edge advancements of this metropolis. It is a place where possibilities seem endless, and dreams are woven into the very fabric of reality. Welcome to a world where innovation and progress converge, creating a captivating backdrop for our tale to unfold."

I hope this captures the essence of the setting for your story! Let me know if you need any further assistance.
You: exit
PS C:\Users\jimmc\Documents\ChatbotProject> python src/CABAL_Tagging_For_ChatBot.py
Chatbot Interface Initialized.
You: uuid: 7547566f-f02e-43d6-9800-bef1e2699622
You: can you provide me a description of the two characters that where provided? 
Chatbot: Absolutely! Here are descriptions for the two characters you've chosen:

1. Jane: Jane is a kind, artistic, and compassionate woman in her late twenties. With her warm smile and gentle demeanor, she has a way of making people feel comfortable around her. Jane has a creative soul, always finding joy in expressing herself through various art forms. She has a natural talent for painting and often loses herself in the vibrant colors that adorn her canvas. Her compassion extends beyond her artwork, as she regularly volunteers at a local shelter, offering her time and support to those in need.

2. Jake: Jake is an adventurous, handy, and determined man in his early thirties. His rugged looks are complemented by his strong physique, a testament to his active lifestyle. Jake thrives on adventure and is always seeking new challenges to conquer. He has a knack for fixing things and can often be found tinkering with gadgets and machinery. Whether it's hiking through breathtaking landscapes or exploring hidden corners of the city, Jake's curiosity knows no bounds. His determination and resourcefulness make him the go-to person for any problem-solving situation.

I hope these descriptions capture the essence of Jane and Jake! Let me know if there's anything else I can assist you with.
You: What colour is Jane's hair?
Chatbot: Jane has beautiful, flowing chestnut brown hair that frames her face elegantly.
You: And her eye colour?
Chatbot: Certainly! What eye color would you like Jane to have?
You: What was her eye colour described as earlier?
Chatbot: I apologize for the confusion. Earlier, Jane's eye color was not mentioned. Please let me know what eye color you would like Jane to have, and I will incorporate it into her description.
You: recallz What was Jane's eye colour described as earlier?
Query for recall: What was Jane's eye colour described as earlier?
Relevant UUIDs: ['d0c581cc-c20e-49f5-be33-3e840f4d0de4', 'a63d3741-a453-430d-becd-f90a5df7c374', 'c6fe8686-f384-48b7-87a9-c5f1b4fd63af', '04bd77db-389f-45a6-a9b8-4822513d97fb', '6f683b3a-ea88-4513-a350-c898f0362bf0']
Chatbot: Apologies for any confusion caused earlier. Jane's eye color was not mentioned in the initial descriptions. If you would like, we can decide on an eye color for Jane now. Please let me know your preference, and I'll be happy to incorporate it into her description.
You: exit