# TheSalesMan Project

## Overview
TheSalesMan is a conversational sales agent named "Steve" that specializes in Apple products. The application utilizes advanced AI capabilities, including Large Language Models (LLMs), to engage users in multi-turn conversations, providing product recommendations and answering queries related to Apple products.

## Features
- Multi-turn conversation capability
- Integration with Mistral AI via Ollama (or any other LLM)
- User configuration options
- Comprehensive data resources for product information
- **LLM-based Relevance Detection:** The system uses an LLM to determine if a user's query is related to Apple products, ensuring that the agent stays focused on its area of expertise.

## Project Structure
```
ThemeSalesMan
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── agent
│   │   ├── __init__.py
│   │   ├── conversation.py
│   │   └── steve.py
│   ├── config
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── data
│   │   ├── __init__.py
│   │   └── resources.py
│   ├── integrations
│   │   ├── __init__.py
│   │   └── llm_integration.py
│   └── utils
│       ├── __init__.py
│       └── helpers.py
├── tests
│   ├── __init__.py
│   ├── test_conversation.py
│   ├── test_steve.py
│   ├── test_settings.py
│   └── test_llm_integration.py
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/prabhat152/ThemeSalesMan.git
   cd ThemeSalesMan
   ```
2. Create a virtual environment (recommended):
   ```
   python3 -m venv venv
   ```
3. Activate the virtual environment:
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     .\venv\Scripts\activate
     ```
4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. **Ensure Ollama is installed and running:**
   This application is now configured to use a local Ollama instance. Please ensure that you have Ollama installed and that the Mistral model (or your preferred model) is available in Ollama.

6. **Set the MISTRAL_API_KEY environment variable:**
   Before running the application, you need to set the `MISTRAL_API_KEY` environment variable. You can obtain an API key from Mistral AI.

   - **On macOS and Linux:**
     ```bash
     export MISTRAL_API_KEY="your_api_key_here"
     ```
   - **On Windows:**
     ```powershell
     $env:MISTRAL_API_KEY="your_api_key_here"
     ```
     (Note: This sets the environment variable for the current session only. To make it permanent, you'll need to set it in the System Properties.)

## Running the Application
To start the conversation agent, run the following command:
```
python src/main.py
```

## Configuration
The application allows for configuration of various parameters in `src/config/settings.py`. The following parameters can be adjusted:
- `temperature`: Controls the randomness of the AI's responses.
- `max_tokens`: Limits the number of tokens in the AI's response.
- `top_p`: Controls the diversity of the output.
- `presence_penalty`: Encourages the model to talk about new topics.
- `frequency_penalty`: Reduces the likelihood of repeated phrases.

## Adding New Data Files
To add new product information or marketing descriptions:
1. Create a new data file in the `src/data` directory.
2. Ensure the file follows the existing structure and format.
3. Update the `resources.py` file to include functions for loading the new data.

## Relevance Detection
The application uses an LLM to determine if a user's query is related to Apple products. This is done by sending a classification prompt to the LLM, which responds with a "yes" or "no" answer. If the query is not related to Apple products, the agent will inform the user that it can only answer questions about Apple products. This ensures that the agent stays focused on its area of expertise and provides relevant responses.

## Testing
To run the tests, use the following command:
```
pytest tests/
```

## License
This project is licensed under the MIT License - see the LICENSE file for details.
