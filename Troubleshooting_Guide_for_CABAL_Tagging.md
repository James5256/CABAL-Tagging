
# Troubleshooting Guide for CABAL-Tagging

This guide aims to help you resolve common issues that you might encounter during the installation and operation of the CABAL-Tagging system.

## Hard-Coded API Key Issues

**Issue**: Errors or security concerns due to hard-coded OpenAI API keys in the source code.

**Solution**:
- **Security Risk**: Avoid storing API keys directly in your source code due to security risks. Instead, use environment variables or a configuration file that is not tracked in your version control system.
- **Refactoring Code**: Modify `ChatbotInterface.py`, `ConversationLogger.py`, and `EmbeddingGenerator.py` to retrieve the API key from an environment variable instead of being hard-coded. Set the environment variable as follows:
  ```bash
  # On Windows
  set OPENAI_API_KEY=your_api_key_here

  # On Unix or MacOS
  export OPENAI_API_KEY=your_api_key_here
  ```
- **Updating Code**: Replace the hard-coded API key in your files with a command to fetch it from the environment variable, e.g., `api_key = os.environ.get('OPENAI_API_KEY')`.

## Python Dependency Issues

**Issue**: Errors related to missing Python packages or incompatible package versions.

**Solution**:
- Ensure all dependencies are installed by running `pip install -r requirements.txt` in your virtual environment.
- If there are version conflicts, try creating a new virtual environment and reinstall the dependencies.

## File Path Errors

**Issue**: Errors related to file paths, especially if the program expects certain directories or files to be in place.

**Solution**:
- Verify that all necessary directories and files exist as expected by the program. This includes logs, embeddings, and other data folders.
- Ensure that paths in your Python scripts are set correctly relative to the project's root directory.

## Unicode or Encoding Issues

**Issue**: Problems with text encoding, often encountered when reading from or writing to files.

**Solution**:
- Make sure your environment and text editors are set to use UTF-8 encoding.
- Explicitly set the encoding to 'utf-8' when opening files in Python.

## General Python Errors

**Issue**: Syntax errors, indentation errors, or runtime exceptions.

**Solution**:
- Check the Python version. The program is designed for Python 3.x.
- Review the error message for hints on what went wrong, and correct any syntax or logical errors in the code.
