
# Installation Guide for CABAL-Tagging

This guide provides detailed steps to install and configure the CABAL-Tagging system on your machine. Ensure you follow these steps after the Git repository is set up.

## Prerequisites

- **Python**: Ensure Python 3.x is installed on your system. It can be downloaded from [python.org](https://www.python.org/downloads/).
- **Git**: Git should be installed for cloning the repository. You can download it from [git-scm.com](https://git-scm.com/).

## Cloning the Repository

Once the Git repository is set up, clone it to your local machine:

```bash
git clone https://github.com/James5256/CABAL-Tagging.git
cd CABAL-Tagging
```

## Setting Up a Virtual Environment (Recommended)

Using a virtual environment is recommended to avoid conflicts with other projects or system-wide packages.

```bash
# Creating a virtual environment
python -m venv venv

# Activating the virtual environment
# Windows
venv\Scripts\activate
# Unix or MacOS
source venv/bin/activate
```

## Installing Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This command installs all necessary dependencies listed in the `requirements.txt` file.

## Additional Configuration

## Setting up environment variables

Set API key for OpenAI:

```bash
export OPENAI_API_KEY='your_api_key_here'
```

## Running the Program

To run the program, use the following command:

```bash
python CABAL_Tagging_For_ChatBot.py
```

## Exiting the Program

You can exit the program by typing `exit` when prompted for user input.

## Troubleshooting

For common issues and solutions that users might encounter during the installation and running of the program, please refer to the [Troubleshooting Guide](Troubleshooting_Guide.md).
