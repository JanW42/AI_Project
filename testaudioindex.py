#pip install SpeechRecognition
#pip install PyAudio
#device_index ist die Audio Input Interface Nummer an dem Gerät an dem das Mirko angeschlossen. Kann 0 - n sein. Die Funktion in testaudioindex.py findet es heraus. Zahl eintragen wo das Hauptmikro hat.
import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))