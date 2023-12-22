
# CABAL-Tagging: Context-Augmented Branch and Leaf Tagging System

## Introduction
CABAL-Tagging, or Context-Augmented Branch and Leaf Tagging, is a chatbot program designed to enhance conversation context management and interaction recall. This system utilizes a combination of current and historical context, making use of unique identifiers (UUIDs) to track and categorize interactions within conversations.

## Features
- **Contextual Awareness**: Utilizes both current and historical context for richer and more relevant chatbot interactions.
- **Branch and Leaf Interaction Management**: Structures conversations as branches, with each message or interaction represented as a leaf, allowing for nuanced tracking and recall.
- **Dynamic UUID Tagging**: Employs UUIDs for categorizing and recalling specific interactions, aiding in effective conversation flow management.

## Modules Overview
- **ChatbotInterface.py**: Handles interactions with the OpenAI API for generating chatbot responses.
- **ConversationLogger.py**: Manages the logging of conversations, including initiation, termination, and summarization.
- **EmbeddingGenerator.py**: Generates embeddings for user inputs and responses, aiding in relevance assessment.
- **RelevanceAssessment.py**: Determines the relevance of past interactions based on embeddings.
- **ContextWindowManager.py**: Controls the context window of conversations, facilitating references to previous interactions.

## Installation
For detailed installation instructions, please see the [Installation Guide](Installation_Guide_for_CABAL_Tagging.md).

## User's Guide
For a comprehensive guide on how to use CABAL-Tagging, refer to the [User's Guide](Users_Guide_CABAL_Tagging.md).

## Troubleshooting
For assistance with common issues during installation and operation, consult the [Troubleshooting Guide](Troubleshooting_Guide_for_CABAL_Tagging.md).

## Examples
For examples of how the program can be used, such as creating a story, recalling past conversation details, or managing conversation context, please see the [Examples](Users_Guide_CABAL_Tagging.md).

## Limitations and Future Work
Note! The script provided is intended as a proof of concept and is intended to be developed upon.
Further to the features displayed in this program, an alternative script to help extract data from a CSV file dataframe, that is relevant to a user's query has also been developed.
This can be made available if the interest is there! 

## Contributing
Contributions are welcome! If you would like to contribute to CABAL-Tagging, please check out our [Contributing Guidelines](CONTRIBUTING.md) for details on how to get started. We appreciate contributions in various forms, including but not limited to code enhancements, bug fixes, documentation improvements, and feature suggestions.

## License
CABAL-Tagging is open source and available under the [MIT License](LICENSE.md). We encourage the use and modification of our code, but we request that all users appropriately reference and acknowledge the original source in their work.