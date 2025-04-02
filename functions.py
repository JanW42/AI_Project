import os
import time
import datetime
import requests
import random
import webbrowser

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        return ("Guten Morgen Sir !")
    elif hour>= 12 and hour<18:
        return("Guten Mittag Sir !")   
    else:
        return("Guten Abend Sir !") 

def functions(query):
    if 'öffne google' in query:
        print("Here you go to Google\n")
        webbrowser.open("google.com")
 
    elif 'öffne stackoverflow' in query:
        print("Here you go to Stack Over flow.Happy coding")
        webbrowser.open("stackoverflow.com")

    elif 'öffne youtube' in query:
        print("Here you go to Youtube\n")
        webbrowser.open("youtube.com")

    elif "wie spät" in query or "wie viel Uhr ist es":
        strTime = datetime.datetime.now().strftime("% H:% M:% S")    
        print(f"Sir, the time is {strTime}")

    elif "wer bist du" in query or "wer hat dich erschaffen" in query or "wer hat dich geschrieben": 
        print("Ich wurde von einer Entwicklergruppe an der FH Münster 2025 erschaffen.")

    elif "ich bin traurig" in query or "mir gehts nicht gut" in query or "ich bin Einsam":  #Witze API
        print("Soll ich dir einen Witz erzählen. Lachen wirkt stresslindern und hat positive Auswirkungen auf ihre physiologische Gesundheit")

    elif "Nachrichten" in query: #API
        pass

    elif "Rechne" in query: #API
        pass
    
    elif "Wetter" in query: #API
        pass

    elif "möchtest du meine Freundin sein" in query or "kannst du meine Freundin sein" in query:   
        print("Ich bin nur ein Programm. Guck doch mal hier. Hier findest du jemanden für dich")
        webbrowser.open("https://hinge.co/de-de")
 
    elif "ich liebe dich" in query:
        print("Das ist kompliziert. Tut mir leid, ich habe mich meiner Aufgabe verschrieben")
    
    elif "Kopiere es hier hin" in query:
        pass

## Sage wenn eine Funktion ausfällt
## Aufgabe mit Rechnenleistung / Leistung erhöhen
    
