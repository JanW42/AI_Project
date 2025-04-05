import speech_recognition as sr
from icecream import ic
#from pydub import AudioSegment
#from pydub.playback import play

#pip install SpeechRecognition

def get_ambient_noise(): #Multithreading
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        recognizer.adjust_for_ambient_noise(source, duration=4)
        #print ("Hintergrundrauschen wurde erfasst")

def record_and_save():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source: #device_index ist die Audio Input Interface Nummer an dem Gerät an dem das Mirko angeschlossen. Kann 0 - n sein. Die Funktion in testaudioindex.py findet es heraus. Zahl eintragen wo das Hauptmikro hat.
        print("Sprich jetzt... (zum Beenden einfach aufhören zu sprechen)")
        while True:
            try:

                audio = recognizer.listen(source, timeout=None)
                print("Sprache erkannt")
                break
            except sr.WaitTimeoutError:
                pass
    
    # Speichere als WAV-Datei (da pydub MP3 nicht direkt unterstützt)
    wav_filename = "input.wav"
    with open(wav_filename, "wb") as f:
        f.write(audio.get_wav_data())
    
    # Konvertiere WAV zu MP3
    #sound = AudioSegment.from_wav(wav_filename)
    #sound.export(filename, format="mp3")
    #print(f"Aufnahme gespeichert als {filename}")

