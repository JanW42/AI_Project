import speech_recognition as sr
#from pydub import AudioSegment
#from pydub.playback import play

def record_and_save():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Sprich jetzt... (zum Beenden einfach aufhören zu sprechen)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, phrase_time_limit=60)
    
    # Speichere als WAV-Datei (da pydub MP3 nicht direkt unterstützt)
    wav_filename = "input.wav"
    with open(wav_filename, "wb") as f:
        f.write(audio.get_wav_data())
    
    # Konvertiere WAV zu MP3
    #sound = AudioSegment.from_wav(wav_filename)
    #sound.export(filename, format="mp3")
    #print(f"Aufnahme gespeichert als {filename}")

