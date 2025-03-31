from config import config
from openai import AzureOpenAI
import edge_tts
import asyncio
import time
import os
from playsound import playsound
from speech_to_text import Speech_to_Text_Parser
from audio_recorder import record_and_save

text = "Hallo mein Name ist Lucy. Ich bin eine künstliche Intelligenz. Wie kann ich dir helfen?"
filename  = "output.mp3"
voice = "de-DE-SeraphinaMultilingualNeural"
rate="+10%"

dir_path = os.path.dirname(os.path.realpath(__file__))

for root, dirs, files in os.walk(dir_path):
    for file in files:
        if file.endswith('output.mp3'):
            print (root+'/'+str(file))
            os.remove(filename)

async def text_to_mp3(text,filename,voice,rate):
    communicate = edge_tts.Communicate(text, voice, rate=rate)
    await communicate.save(filename)
    print(f"Saved {filename}")
  
def create_message(prompt):
    model = "gpt4o"   #definiere Model von ChatGpt


    #Nachfolgende OpenAIModel und if Funktion Optional
    OpenAIModels = {
        "gpt4o": "gpt4o",
        "gpt-4": "gpt-4",
        "gpt-4-turbo": "gpt-4-turbo",
        "gpt-3.5-turbo": "gpt-3.5-turbo",
        "text-davinci-003": "text-davinci-003",
        "text-embedding-3-large": "embed",      # Große Vektor (z. B. 1536 Dimensionen)
        "text-embedding-3-small": "embeddings", # Kleine Vektor (z. B. 384 Dimensionen)
        "dall-e-3": "dall-e-3",
        "whisper-1": "whisper-1",
        "o1": "o1",
        "o1-mini": "o1-mini",
        "o3": "o3",
        "o3-mini": "o3-mini"
    }
    
    if model not in OpenAIModels:
        raise ValueError(f"Das Modell {model} wird nicht unterstützt. "
                         f"Verfügbare Modelle: {list(OpenAIModels.keys())}")


    # Auswahl des entsprechenden Deployments
    selected_deployment = OpenAIModels[model]

    # Erstellen des AzureOpenAI-Clients
    client = AzureOpenAI(
        api_key=config.AZURE_OPENAI_API_KEY,
        azure_endpoint=config.AZURE_OPENAI_ENDPOINT,
        api_version=config.OPENAI_API_VERSION,
        azure_deployment=selected_deployment
    )

    #Erstelle eine Nachricht die im passenend Format für ChatGpt API. Packe den prompt herein
    messages = [
        {"role": "user", "content": prompt}
    ]

    #Frage nach bei der API. Sende dafür die Nachricht mit dem GPT Model was zur Antwort benutzt werden soll.
    response = client.chat.completions.create(messages=messages, model=model)
    return response.choices[0].message.content   #Gebe die Antwort die in im ersten Choise Eintrag unter Content steht aus.

asyncio.run(text_to_mp3(text, filename, voice, rate))
time.sleep(1)
try:
    playsound(filename)



    os.remove(filename)
except Exception as e:
    print (e)

while True:
    try:
        #Version 1 nur Commandozeile nächste Zeile
        #Frage = input("Hallo, stelle mir eine Frage. Ctrl+C zum Beenden. ")
        record_and_save() #Hier wird die Funktion record and save aufgerufen um die Mikrosprache solange auszunehmen bis man aufhört zu reden. Dann wird es in der Input.wav Datei gespeichert.
        text = Speech_to_Text_Parser() #Hier wird die Sprache aus input.mp3 in Text verarbeitet mit der extrem Leistungsstarken lokalen CUDA anwendung von OpenAI / Nvidia
        result = create_message(text)  #Rufe die Funktion auf und übergebe die "Frage" zu ChatGpt API
        #Alte Version nur mit Commandozeile. Die nächsten beiden Zeilen.
        #result = create_message(Frage)  #Rufe die Funktion auf und übergebe die "Frage" zu ChatGpt API
        #print(result) #Gebe die Antwort in der Commandozeile aus.
        asyncio.run(text_to_mp3(result, filename, voice, rate))
        try:
            playsound(filename)
            os.remove(filename)
        except Exception as e:
            print (e)
    except Exception as e:
        print (e)
