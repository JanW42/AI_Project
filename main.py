import os
import re
import time
import asyncio
import edge_tts #pip install edge_tts
from config import config #Lokal eigene Lib
from settings import settings #Lokal eigene Lib
from openai import AzureOpenAI #pip install openai
from playsound import playsound #pip install playsound==1.2.2
from audio_recorder import record_and_save, get_ambient_noise #Lokal eigene Lib
from speech_to_text import Speech_to_Text_Parser, set_cuda_paths #Lokal eigene Lib
from icecream import ic


def initial_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(dir_path):  # Nur Dateien im Root-Ordner auflisten
        file_path = os.path.join(dir_path, file) #stellt sicher, dass richtiges Trennzeichen MacOs Windows
        if file.endswith(settings.filename):   #zur wav datei machen für mehr performance!
            print (file_path+'/'+str(file))
            os.remove(settings.filename) #Datei löschen wenn mp3 vorhanden
            ic()
            
## async ist eine besondere Funktion. Asynchrones Programmieren. Nicht so wie das Normale synchrone was codezeile nach codezeile in einer Abfolge abarbeitet. Hier braucht man auch besondere Syntax, async und await. async initialisiert und await lässt der Code an der stelle stehen und es werden keine neuen Ressourcen freigeben. Ist fortgeschrittnes Python programmieren braucht man aber hier. Threding hilfreich zu verstehen um das zu verstehen.
async def text_to_mp3(welcometext,filename,voice,rate):
    ic()
    print("Text zu Mp3 starten")
    communicate = edge_tts.Communicate(welcometext, voice, rate=rate)
    await communicate.save(settings.filename)  ## warte bis file gespeichert bevor codezeile verlassen wird.
    #print(f"Saved {filename}")
    ic()
    print("Text zu Mp3 gespeichert")

def remove_asterisks(welcometext):
    #Entfernt alle Sternchen (*) und (-) aus dem GPT content.
    # return: String ohne * und -
    return re.sub(r'[\*-]', '', welcometext)
    
def create_message(prompt):
    ic()
    print("Text zu Audio fertig")
    model = settings.model   #definiere Model von ChatGpt

    #Nachfolgende OpenAIModel und if Funktion Optional
    OpenAIModels = settings.OpenAIModels
    
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
    response_content = response.choices[0].message.content
    ic()
    print("Zeichen aus der GPT_Antwort Anfang")
    response_without_asterisks = remove_asterisks(response_content) #Sonderzeichen die im GPT Output stehen entfernen für bessere Sprachausgabe
    ic()
    print("Zeichen aus der GPT_Antwort Ende")
    ic()
    print("Antwort von GPT_API")
    print (response_without_asterisks)
    return response_without_asterisks


if __name__ == "__main__":
    initial_path()
    asyncio.run(text_to_mp3(settings.welcometext, settings.filename, settings.voice, settings.rate))
    try:
        playsound(settings.filename)
        os.remove(settings.filename)
    except Exception as e:
        print (e)
        raise RuntimeError("Exception in first playsound")

    set_cuda_paths()# Setzte einmal den CUDA Pfad
    get_ambient_noise()# Erfasse Hintergrundrauschen

    while True:
        try:
            record_and_save() #Hier wird die Funktion record and save aufgerufen um die Mikrosprache solange auszunehmen bis man aufhört zu reden. Dann wird es in der Input.wav Datei gespeichert.
            text = Speech_to_Text_Parser() #Hier wird die Sprache aus input.mp3 in Text verarbeitet mit der extrem Leistungsstarken lokalen CUDA anwendung von OpenAI / Nvidia
            result = create_message(text)  #Rufe die Funktion auf und übergebe die "Frage" zu ChatGpt API
            asyncio.run(text_to_mp3(result, settings.filename, settings.voice, settings.rate))
            try:
                ic()
                print("Audio Datei fertig gleich abspielen")
                playsound(settings.filename) # Den im neuem Thread starten um dazwischen zu sprechen
                os.remove(settings.filename)
            except Exception as e:
                print (e)
                raise RuntimeError("Exception in playsound in While True")
        except Exception as e:
            print (e)
            raise RuntimeError("Exception in Haupt While True")
