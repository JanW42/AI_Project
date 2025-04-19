[![Tests](https://pypi-camo.freetls.fastly.net/bdbd035da2ab4288a104e1bea66187e52fa0c51b/68747470733a2f2f6769746875622e636f6d2f6d6174706c6f746c69622f6d6174706c6f746c69622f776f726b666c6f77732f54657374732f62616467652e737667)](https://github.com/JanW42/AI_Project/pulls)
[![Status](https://pypi-camo.freetls.fastly.net/5d2da640fa2fb42f1cab6f8bf77084d0e539d17f/68747470733a2f2f696d672e736869656c64732e696f2f707970692f7374617475732f5370656563685265636f676e6974696f6e2e737667)](https://github.com/JanW42/AI_Project/issues)
[![GitHub Issues](https://pypi-camo.freetls.fastly.net/52bea5a66ac819c8d1c22a8ef9f2075d7b153a03/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f69737375655f747261636b696e672d6769746875622d626c75652e737667)](https://github.com/JanW42/AI_Project/issues)

# AI_Project

AI Voice Assistant Alessa. Project at the FH Münster with Dr. Rasch in Prescriptive Analytics and Artificial Intelligence

## Structure
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [File Details](#file-details)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [Acknowledgments](#acknowledgments)

## Overview

**AI_Project** is a AI Voice Assistent designed to answer questions:
1. It will retrieves relevant chunks of text from local PDF documents.
2. It calls Azure OpenAI to generate context-aware responses.
3. It will fetches real-time weather information via the OpenWeather API.
4. It will displays everything in a Real-Time WebApp.

## Features

- **AI Voice Assistent**: An AI with emotional german voice to answer questions using gpt4o Openai API.
- **Local PDF Retriever**: Will use chunk-based embedding retrieval to provide context for your questions.
- **Azure OpenAI Integration**: Generates answers using GPT models hosted on Azure OpenAI.
- **OpenWeather API**: Retrieves up-to-date weather information for a given location.
- **Datetime now**: Tells you the current time.

## Project Structure

```plaintext
├── main.py                      # AI Assistant using Opanai API
├── performance_tracking.py      # Contains a function to which all functions are passed so that the runtime can be measured within a method
├── hotword_call_and_action.py   # Script that provides all functions for audio recording and storage for further processing
├── speech_to_text.py            # The script that provides all language functions for text conversion. Built on faster_whisper. An extremely powerful stt CUDA GPU usage
├── text_to_speech.py            # Script that provides all functions for text to speech process
├── testaudioindex.py            # A test script to find out the audio interface index to start real-time voice input
├── settings.py                  # Script that contains all variables to set them without much effort
├── requirements.txt             # Python dependencies
├── config.py                    # Holds environment variables (.gitignore)
└── README.md                    # Documentation (this file)
```

### File Details

- `main.py`
  
- `audio_recorder.py`

- `speech_to_text.py`

- `staudioindex.py`

- `config.py`
> [!CAUTION]
> A file that contains environment variables such as API keys and endpoints.  
> Not tracked by Git for security (make sure your `.gitignore` is set correctly).

## Requirements
> [!IMPORTANT]
> Install Python v.3.10.5 find here www.python.org

## Installation
**1. Get started**:

```bash
python.exe -m pip install --upgrade pip
py --list
```
Check Python Versions installt here should now be -V : 3.10 now.
 

If there are errors when installing playsound
```bash
pip install --upgrade setuptools wheel
pip install playsound
```

Install GitLens Extansion (Ctrl+Shift+X)de - Type in “GitLens”. 
After this open files or folders in VS Code (Ctrl+K F)de. 
Create an empty folder in the location of your choice. 
Open this folder (Ctrl+K Ctrl+O)de. 
Go to the Git version management (Ctrl+Shift+G)de. 
Go to Clone Repo. 
Finally login into GitHub. 

**Add necessary settings**
```bash
git --global user.name "Your name for commits"
git --global user.email "Your E-Mail for commits"
```
**Final steps to graphic commit**
Type a commit message above (this will be displayed in GitHub).
The press Changes [+] to pack all changes into stages.
Finally [Sync Changes 1].
   
Done :rocket: Code has been successfully pushed to GitHub

**2. Clone this repository**:
> [!TIP]
> Press (Shift+right Mouse) here you want the Folder -> open Powershell Window here.

```bash
git clone https://github.com/JanW42/AI_Project.git
cd AI_Project
```

**3. Create and activate a virtual environment (optional but recommended)**:
> [!TIP]
> Open the AI_Project Folder with VSCode.
> Open a new Terminal with (Ctrl+Shift+ö)de.

```bash
python -3.10 -m venv VE   # "VE" is the name of the virtual Environment
or
py -3.10 -m venv VE
source VE/bin/activate    # for macOS / Linux
VE\Scripts\activate.bat   # for Windows using cmd
VE\Scripts\activate.ps1   # for Windows using PowerShell
```

> [!TIP]
> Now the VE is active, you see it as it is at the beginning at the code line and
> at the bottom right is now {} Python 3.10.5('VE':venv)

**4. Install required dependencies**:
```bash
pip install -r requirements.txt
```

> [!TIP]
> Install manually if import library name is still underlined in yellow.
> Ctrl+Shift+P “Reload Window” before.

```bash
pip install time
pip install edge_tts
pip install openai
pip install playsound==1.2.2
pip install SpeechRecognition
pip install faster-whisper
pip install pyaudio
pip install torch==2.6.0
pip install torchaudio==2.6.0
pip install nvidia-cudnn-cu12==9.5.0.50
pip install nvidia-cuda-nvrtc-cu12==12.4.127
pip install nvidia-cuda-runtime-cu12==12.4.127
pip install nvidia-cublas-cu12==12.4.5.8
```
**5. Set up your environment variables** in `config.py` (see [Configuration](#configuration)).

## Usage

1. **Prepare your PDFs:**  
   - Place any relevant PDF documents in the `data` folder (or whichever folder you specify in `retriever.py`)

2. **Run the application:**
   - Start normal with the play button or in terminal 'main.py'
   
3. **Interact:**
   - Wait till Alessa talks  
   - Ask your question

## Configuration
> [!IMPORTANT]
> Create a file named `config.py` and add following environment variables (example structure):

```python
from dataclasses import dataclass

#Why do we use the built-in data class? They are robust and thread-safe. Still important for later app

@dataclass
class config:
   # Azure OpenAI
   AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
   AZURE_OPENAI_ENDPOINT="https://your-azure-endpoint.openai.azure.com/"
   OPENAI_API_VERSION="2023-06-15-preview"

   # OpenWeather
   WEATHER_API_KEY="your_openweather_api_key"
```

> [!CAUTION]
> Make sure **config.py** is referenced in your `.gitignore` so that it is not pushed to GitHub, keeping your keys safe. Your .gitignore should look like this.

```python
##Get latest from https://github.com/github/gitignore/blob/main/VisualStudio.gitignore
config.py
config.txt
VE/  #change VE when using another venv name
*.log
*.wav
*.mp3
```

## How It Works

## Contributing

Contributions, issues, and feature requests are welcome!  
Feel free to check the [issues page](../../issues) to see if your idea or bug report has already been mentioned, or open a new one.

## Acknowledgments

- [`edge_tts`](https://github.com/rany2/edge-tts) for providing a emotional text to Voice.
- [`speech_recognition`](https://github.com/Uberi/speech_recognition) for providing a fast smart way to save audioinput into .wav files.  
- [`playsound`](https://github.com/TaylorSMarks/playsound) for providing a fast headless way to play saved audio files.
- [`faster_whisper`](https://github.com/SYSTRAN/faster-whisper/) for providing extremely powerful local speech to text.
- [`AzureOpenAI`](https://github.com/openai/openai-python/tree/main) for hosting GPT models.  
- [`OpenWeather`](https://openweathermap.org) for real-time weather data.  
- **You** for trying out this tool!

---
