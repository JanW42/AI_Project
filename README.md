# AI_Project

AI voice assistant Lucy. Project at Dr. Rasch in EM Prescriptive Analytics and Artificial Intelligence

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

**AI_Project** is a chatbot-like application designed to answer questions:
1. It retrieves relevant chunks of text from local PDF documents.
2. It calls Azure OpenAI to generate context-aware responses.
3. It fetches real-time weather information via the OpenWeather API.
4. It displays everything in a App.

## Features

- **AI Voice Assistent**: An Ai with emotional german voice to complete tasks and access to gpt4o API.
- **Local PDF Retriever**: Uses chunk-based embedding retrieval to provide context for your questions.
- **Azure OpenAI Integration**: Generates answers using GPT models hosted on Azure OpenAI.
- **OpenWeather API**: Retrieves up-to-date weather information for a given location.
- **Customizable Prompt Template**: You can define your own prompt structure in a simple text file.

## Project Structure

```plaintext
├── main.py               # AI Assistant using Opanai API
├── audio_recorder.py     # Script that provides all functions for audio recording and storage for further processing
├── speech_to_text.py     # The script that provides all language functions for text conversion. Built on faster_whisper. An extremely powerful stt CUDA GPU usage
├── testaudioindex.py     # A test script to find out the audio interface index to start real-time voice input
├── requirements.txt      # Python dependencies
├── config.py             # Holds environment variables (not tracked by Git)
└── README.md             # Documentation (this file)
```

### File Details

1. **main.py**  
  
2. **audio_recorder.py**  

3. **speech_to_text.py**  

4. **testaudioindex.py**  
   - A text file containing placeholders (like `{input_text}`, `{kontext}`, and `{weather}`) to create a final prompt.

5. **config.py**  
   - A file that contains environment variables such as API keys and endpoints.  
   - Not tracked by Git for security (make sure your `.gitignore` is set correctly).

## Installation
1. **Configuriere git**:
   - Installiere GitLens Extansion (Ctrl+Shift+X) - Tippe ein "GitLens"
   - Schließe geöffnete Dateien oder Ordner/Folder in VS Code (Ctrl+K F)
   - Erstelle einen leeren Ordner am Speicherort deiner Wahl
   - Öffne diesen Ordner (Ctrl+K Ctrl+O)
   - Gehe auf das Git Versionsverwaltung (Ctrl+Shift+G)
   - Gehe auf Clone Repo
   - Login into GitHub

   **Add necessary settings**
   ```bash
   git --global user.name "Dein Name für Commits"
   git --global user.email "Deine Email für Commits"
   ```
   **Final steps to graphic commit**
   - Tippe eine commit Nachricht oben ein (diese wird in GitHub angezeigt)
   - Drücke auf Changes [+] um alle Changes in Stages zu packen
   - Drücke auf [Sync Changes 1]
   
   - Fertig - Code wurde erfolgreich auf GitHub gepusht

2. **Clone this repository**:
   - Under Windows go there you want the new Folder with the Code and there:
   - Press (Shift+right Mouse) -> open Powershell Window here


    ```bash
    git clone https://github.com/JanW42/AI_Project.git
    cd AI_Project
    ```

3. **Create and activate a virtual environment (optional but recommended)**:
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
4. **Install required dependencies**:
   - Also now in the same terminal

    ```bash
    pip install -r requirements.txt
    ```

5. **Set up your environment variables** in `config.txt` (see [Configuration](#configuration)).

## Usage

1. **Prepare your PDFs**:  
   - Place any relevant PDF documents in the `data` folder (or whichever folder you specify in `retriever.py`).

2. **Run the application**:
   
3. **Interact**:  
   - Wait till Lucy talks.  
   - Say your question. Wait 1 Seconds before talking to let the skricpt get all Data.  

## Configuration

Create a file named `config.py` and add following environment variables (example structure):

```dotenv
# Azure OpenAI
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_ENDPOINT=https://your-azure-endpoint.openai.azure.com/
OPENAI_API_VERSION=2023-06-15-preview

# OpenWeather
WEATHER_API_KEY=your_openweather_api_key
```

Make sure **config.py** is referenced in your `.gitignore` so that it is not pushed to GitHub, keeping your keys safe.

## How It Works

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](../../issues) to see if your idea or bug report has already been mentioned, or open a new one.

## Acknowledgments

- **speech_recognition**: For providing a fast smart way to save audioinput into .wav files.  
- **faster_whisper**:  For providing extremely powerful local language models that run on CUDA Nvidia GPU and this work almost in real time.
- **Azure OpenAI**: For hosting GPT models.  
- **OpenWeather**: For real-time weather data.  
- **You**: For trying out this tool!

---
