import os, asyncio
from config import config #Lokal eigene Lib
from settings import settings #Lokal eigene Lib
from openai import AzureOpenAI #pip install openai
from playsound import playsound #pip install playsound==1.2.2
from hotword_call_and_action import record_and_save, get_ambient_noise, hotword_call_and_action #Lokal eigene Lib
from speech_to_text import Speech_to_Text_Parser, set_cuda_paths #Lokal eigene Lib
from text_to_speech import remove_asterisks, text_to_mp3
from icecream import ic
from performance_tracking import time_function

def initial_path():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    for file in os.listdir(dir_path):  # Nur Dateien im Root-Ordner auflisten
        file_path = os.path.join(dir_path, file) #stellt sicher, dass richtiges Trennzeichen MacOs Windows
        if file.endswith(settings.filename):   #zur wav datei machen für mehr performance!
            print (file_path+'/'+str(file))
            os.remove(settings.filename) #Datei löschen wenn mp3 vorhanden
                
def create_message(prompt):
    model = settings.model   #definiere Model von ChatGpt

    # Nachfolgende OpenAIModel und if Funktion Optional
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

    # Erstelle eine Nachricht die im passenend Format für ChatGpt API. Packe den prompt herein
    messages = [
        {"role": "user", "content": prompt}
    ]

    # Frage nach bei der API. Sende dafür die Nachricht mit dem GPT Model was zur Antwort benutzt werden soll.
    response = client.chat.completions.create(messages=messages, model=model)
    response_content = response.choices[0].message.content
    response_without_asterisks = remove_asterisks(response_content) #Sonderzeichen die im GPT Output stehen entfernen für bessere Sprachausgabe
    return response_without_asterisks


if __name__ == "__main__":
    time_function(initial_path)
    asyncio.run(text_to_mp3(settings.welcometext, settings.filename, settings.voice, settings.rate, settings.pitch))
    try:
        time_function(playsound, settings.filename)
        time_function(os.remove, settings.filename)
    except (RuntimeError, TypeError, ValueError) as e:
        print (f'Error in Initial playsound True. {e}')
    except KeyboardInterrupt:
        print ("Das Programm wurde beendet")

    time_function(set_cuda_paths)# Setzte einmal den CUDA Pfad
    #time_function(get_ambient_noise)# Erfasse Hintergrundrauschen

    while True:
        try:
            status, text = hotword_call_and_action()
            #time_function(record_and_save) #Hier wird die Funktion record and save aufgerufen um die Mikrosprache solange auszunehmen bis man aufhört zu reden. Dann wird es in der Input.wav Datei gespeichert.
            #text = time_function(Speech_to_Text_Parser) #Hier wird die Sprache aus input.mp3 in Text verarbeitet mit der extrem Leistungsstarken lokalen CUDA anwendung von OpenAI / Nvidia
            if status:
                time_function(playsound, "tmp77bgpy50.mp3")
                break
            result = time_function(create_message, text)  #Rufe die Funktion auf und übergebe die "Frage" zu ChatGpt API
            asyncio.run(text_to_mp3(result, settings.filename, settings.voice, settings.rate, settings.pitch))
            try:
                time_function(playsound, settings.filename)
                time_function(os.remove, settings.filename)

            except (RuntimeError, TypeError, ValueError) as e:
                print (f'Error in Haupt While True. {e}')

        except (RuntimeError, TypeError, ValueError) as e:
            print (f'Error in Hauptwhile True. {e}')
        except KeyboardInterrupt:
            print ("Programm wurde beendet")
