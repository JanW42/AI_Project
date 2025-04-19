import speech_recognition as sr #pip install SpeechRecognition
from icecream import ic

                   
from config import config
import requests
from datetime import datetime
import asyncio, os, re
from text_to_speech import text_to_mp3
from performance_tracking import time_function

def get_ambient_noise():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        recognizer.adjust_for_ambient_noise(source, duration=4)

def record_and_save():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Sprich jetzt... (zum Beenden einfach aufhören zu sprechen)")
        while True:
            try:

                audio = recognizer.listen(source, timeout=None)
                print("Sprache erkannt")
                break
            except sr.WaitTimeoutError:
                pass
    
    wav_filename = "input.wav"
    with open(wav_filename, "wb") as f:
        f.write(audio.get_wav_data())

    

def hotword_call_and_action():
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone(device_index=1) as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            print("Sage 'Alessa'")
            audio = recognizer.listen(mic)

            wav_filename = "input.wav"
            with open(wav_filename, "wb") as f:
                f.write(audio.get_wav_data())
            from speech_to_text import Speech_to_Text_Parser
            from settings import settings

            from faster_whisper import WhisperModel
            model_size = settings.model_size
            try:
                model = WhisperModel(model_size, device=settings.device, compute_type=settings.compute_type)
            except RuntimeError:
                continue
            segments, info = model.transcribe("input.wav", beam_size=5)
            for segment in segments:
                print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
            text = segment.text

            if "Alessa" in text:
                from playsound import playsound
                playsound("tmpk062s683.mp3")
                print("Stelle mir deine Frage...")
                audio = recognizer.listen(mic, timeout=None)

                wav_filename = "input.wav"
                with open(wav_filename, "wb") as f:
                    f.write(audio.get_wav_data())
                from speech_to_text import Speech_to_Text_Parser

                model_size = settings.model_size
                model = WhisperModel(model_size, device=settings.device, compute_type=settings.compute_type)
                segments, info = model.transcribe("input.wav", beam_size=5)
                for segment in segments:
                    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
                text = segment.text
                if "Stopp" in text:
                    status = True
                    text = ""
                    return status, text
                
                if "Wetter" in text:
                    playsound ("tmpw79o6tmd.mp3")
                    print("Sage jetzt welche Stadt...")
                    audio = recognizer.listen(mic, timeout=None)

                    wav_filename = "input.wav"
                    with open(wav_filename, "wb") as f:
                        f.write(audio.get_wav_data())
                    
                    model_size = settings.model_size
                    model = WhisperModel(model_size, device=settings.device, compute_type=settings.compute_type)
                    segments, info = model.transcribe("input.wav", beam_size=5)
                    for segment in segments:
                        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

                    text = segment.text
                    text = text.strip()
                    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

                    weather = get_openweather(text)

                    asyncio.run(text_to_mp3(weather, settings.filename, settings.voice, settings.rate, settings.pitch))
                    time_function(playsound, settings.filename) # Den im neuem Thread starten um dazwischen zu sprechen
                    time_function(os.remove, settings.filename)
                    continue
                
                if "Kurs" in text:
                    playsound ("tmpb8ofst0s.mp3")
                    continue
                
                if "Uhr" in text:
                    time = datetime.now()
                    time = time.strftime("%H:%M:%S")

                    asyncio.run(text_to_mp3(f"Es ist {time}", settings.filename, settings.voice, settings.rate, settings.pitch))
                    time_function(playsound, settings.filename) # Den im neuem Thread starten um dazwischen zu sprechen
                    time_function(os.remove, settings.filename)
                    continue
                
                if "spät" in text:
                    time = datetime.now()
                    time = time.strftime("%H:%M:%S")

                    asyncio.run(text_to_mp3(time, settings.filename, settings.voice, settings.rate, settings.pitch))
                    time_function(playsound, settings.filename) # Den im neuem Thread starten um dazwischen zu sprechen
                    time_function(os.remove, settings.filename)
                    continue
                else:
                    if text is not None:
                        status = False
                        return status, text
            print("\033[38;2;255;165;0mHotword Failed\033[0m")

def get_openweather(stadt: str):
    WEATHER_API_KEY = config.WEATHER_API_KEY

    if not WEATHER_API_KEY:
        raise EnvironmentError("Fehlende Umgebungsvariablen. Bitte prüfen Sie die 'config.txt'-Datei.")

    url = f"http://api.openweathermap.org/data/2.5/weather?q={stadt}&appid={WEATHER_API_KEY}&units=metric&lang=de"
    response = requests.get(url)
    data = response.json()
    
    if data.get("cod") == 200:
        temp = data["main"]["temp"]
        wetterbeschreibung = data["weather"][0]["description"]
        return f"Das aktuelle Wetter in {stadt} ist {wetterbeschreibung} bei {temp}°C."
    else:
        return "Entschuldigung, das Wetter konnte nicht abgerufen werden."