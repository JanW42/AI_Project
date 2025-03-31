# AI_Project

Own AI assistant. Project at Dr. Rasch in EM Prescriptive Analytics and Artificial Intelligence

Achtung Readme ist im Rohbau!!!! Nur für Formatierung/Syntax Übernommen.

## Structure
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Overview

**AI_Project** is a chatbot-like application designed to answer travel-related questions:
1. It retrieves relevant chunks of text from local PDF documents (e.g., travel guides).
2. It calls Azure OpenAI to generate context-aware responses.
3. It fetches real-time weather information via the OpenWeather API.
4. It displays everything in a user-friendly Streamlit interface with a custom background image and styling.

## Features

- **Streamlit Web App**: A clean UI that allows users to input queries.
- **Local PDF Retriever**: Uses chunk-based embedding retrieval to provide context for your questions.
- **Azure OpenAI Integration**: Generates answers using GPT models hosted on Azure OpenAI.
- **OpenWeather API**: Retrieves up-to-date weather information for a given location.
- **Customizable Prompt Template**: You can define your own prompt structure in a simple text file.

## Project Structure

```plaintext
├── main.py               # Streamlit app entry point
├── retriever.py          # Contains functions to handle PDF chunking and embedding-based retrieval
├── llm_utils_client.py   # Utilities for connecting to Azure OpenAI and OpenWeather
├── content_template.txt  # A template used to format the final prompt
├── requirements.txt      # Python dependencies
├── config.txt            # Holds environment variables (not tracked by Git)
└── README.md             # Documentation (this file)
```

### File Details

1. **main.py**  
   - Launches the Streamlit application.  
   - Loads a prompt template and processes user input.  
   - Calls the `dense_retriever` function from `retriever.py` to find relevant document chunks.  
   - Calls `get_openweather` from `llm_utils_client.py` to get real-time weather data.  
   - Passes all data to Azure OpenAI to generate a context-enriched response.

2. **retriever.py**  
   - Converts PDFs into text chunks (via `pdf_to_text_chunks` or `folder_to_text_chunks`).  
   - Computes embeddings for the chunks and the user query.  
   - Performs a **dense retrieval** by comparing embeddings via cosine similarity.  
   - Returns the most relevant chunks to be used by the main application.

3. **llm_utils_client.py**  
   - Provides a function to create an **AzureOpenAI** client for GPT-based models.  
   - Fetches **OpenWeather** data for a given city using your API key.  

4. **content_template.txt**  
   - A text file containing placeholders (like `{input_text}`, `{kontext}`, and `{weather}`) to create a final prompt.

5. **config.txt**  
   - A file that contains environment variables such as API keys and endpoints.  
   - Not tracked by Git for security (make sure your `.gitignore` is set correctly).

## Installation
0. **Configuriere git**
   - Installiere GitLens Extansion (Ctrl+Shift+X) - Tippe ein "GitLens"
   - Schließe geöffnete Dateien oder Ordner/Folder in VS Code (Ctrl+K F)
   - Erstelle einen leeren Ordner am Speicherort deiner Wahl
   - Öffne diesen Ordner (Ctrl+K Ctrl+O)
   - Gehe auf das Git Versionsverwaltung (Ctrl+Shift+G)
   - Gehe auf Clone Repo
   - Login into GitHub


   ```bash
   git --global user.name "Dein Name für Commits"
   git --global user.email "Deine Email für Commits"
   ```

   - Tippe eine commit Nachricht oben ein (diese wird in GitHub angezeigt)
   - Drücke auf Changes [+] um alle Changes in Stages zu packen
   - Drücke auf [Sync Changes 1]
   
   - Fertig - Code wurde erfolgreich auf GitHub gepusht

1. **Clone this repository**:
   - Under Windows go there you want the new Folder with the Code and there:
   - Press (Shift+right Mouse) -> open Powershell Window here


    ```bash
    git clone https://github.com/JanW42/AI_Project.git
    cd AI_Project
    ```

2. **Create and activate a virtual environment (optional but recommended)**:
   - Open your new AI_Project Folder with VSCode
   - Open a new Terminal with (Ctrl+Shift+ö)


    ```bash
    python -m venv ai         # "ai" is the Name of the virtual Environment
    source ai/bin/activate    # for macOS / Linux
    ai\Scripts\activate.bat   # for Windows using cmd
    ai\Scripts\activate.ps1   # for Windows using PowerShell
    ```
   - Now the VE is active, you see it as it is at the beginning at the code line and
   - at the bottom right is now {} Python 3.10.5('VE':venv)
3. **Install required dependencies**:
   - Also now in the same terminal

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up your environment variables** in `config.txt` (see [Configuration](#configuration)).

## Usage

1. **Prepare your PDFs**  
   - Place any relevant PDF documents in the `data` folder (or whichever folder you specify in `retriever.py`).

2. **Run the application**:
    ```bash
    streamlit run main.py
    ```
3. **Interact**  
   - Open the displayed URL in your web browser.  
   - Type your travel queries or any question.  
   - The app will show the context from your PDF files and the current weather in the chat response.

## Configuration

Create a file named `config.txt` (or modify the existing one) with the following environment variables (example structure):

```dotenv
# Azure OpenAI
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-azure-endpoint.openai.azure.com/
OPENAI_API_VERSION=2023-06-15-preview

# OpenWeather
WEATHER_API_KEY=your_openweather_api_key
```

Make sure **config.txt** is referenced in your `.gitignore` so that it is not pushed to GitHub, keeping your keys safe.

## How It Works

1. **User Query**: The user inputs a question or statement in the Streamlit interface.
2. **Document Retrieval**: 
   - `dense_retriever()` uses a PDF chunking and embedding approach to find the most relevant text chunks from local PDFs.
3. **Weather Data**:
   - `get_openweather()` fetches the current weather for a given city (e.g., "Lissabon").
4. **Azure OpenAI Prompt**:
   - The content template (`content_template.txt`) is loaded and formatted with placeholders for user input, relevant PDF chunks, and weather data.
   - The prompt is sent to your Azure OpenAI deployment (GPT-4o, text-embedding-3-large).
5. **Response**:
   - Azure OpenAI returns a response, which is then displayed in the Streamlit app alongside user queries, mimicking a chat experience.

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](../../issues) to see if your idea or bug report has already been mentioned, or open a new one.


## Acknowledgments

- **Streamlit**: For providing a fast way to build web apps in Python.  
- **LangChain Community**: For robust document loaders and text-splitting utilities.  
- **Azure OpenAI**: For hosting GPT models.  
- **OpenWeather**: For real-time weather data.  
- **You**: For trying out this tool!

---
