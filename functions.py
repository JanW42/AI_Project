import os
import time
import datetime
import requests
import random
import webbrowser

## Das ist eine datei um Ideen zu sammeln. später kann diese alle funktionen halten und der Kern sein auf den der AI Voice Assistent zugreift
##
##

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<12:
        return ("Guten Morgen Sir !")
    elif hour>= 12 and hour<18:
        return("Guten Mittag Sir !")   
    else:
        return("Guten Abend Sir !") 

def functions(query):


    ## Einfache Funktionen
    if 'öffne google' in query:
        print("Here you go to Google\n") #print natürlich ersetzten und noch zu text_to_speech schicken
        webbrowser.open("google.com")
 
    elif 'öffne stackoverflow' in query:
        print("Here you go to Stack Over flow.Happy coding") #print natürlich ersetzten und noch zu text_to_speech schicken
        webbrowser.open("stackoverflow.com")

    elif 'öffne youtube' in query:
        print("Here you go to Youtube\n") #print natürlich ersetzten und noch zu text_to_speech schicken
        webbrowser.open("youtube.com") 

    elif "wie spät" in query or "wie viel Uhr ist es":
        strTime = datetime.datetime.now().strftime("% H:% M:% S")    
        print(f"Sir, the time is {strTime}") #print natürlich ersetzten und noch zu text_to_speech schicken

    elif "wer bist du" in query or "wer hat dich erschaffen" in query or "wer hat dich geschrieben": 
        print("Ich wurde von einer Entwicklergruppe an der FH Münster 2025 erschaffen.") #print natürlich ersetzten und noch zu text_to_speech schicken

    elif "ich bin traurig" in query or "mir gehts nicht gut" in query or "ich bin Einsam":  #Witze API
        print("Soll ich dir einen Witz erzählen. Lachen wirkt stresslindern und hat positive Auswirkungen auf ihre physiologische Gesundheit") #print natürlich ersetzten und noch zu text_to_speech schicken



    ## Ein bisschen Humor. Einfache funktionen
    elif "möchtest du meine Freundin sein" in query or "kannst du meine Freundin sein" in query:   
        print("Ich bin nur ein Programm. Guck doch mal hier. Hier findest du jemanden für dich") #print natürlich ersetzten und noch zu text_to_speech schicken
        webbrowser.open("https://hinge.co/de-de")
 
    elif "ich liebe dich" in query:
        print("Das ist kompliziert. Tut mir leid, ich habe mich meiner Aufgabe verschrieben") #print natürlich ersetzten und noch zu text_to_speech schicken
    
    ## Komplexere Funktionen mit API zugriff. Auch deutlich interessanter. Bietet mehr Potenzial
    elif "Nachrichten" in query: #API
        pass
    
    elif "Wetter" in query: #API
        pass

    ## Potenzial für außerordentlich Herausragende Aufgabe
    ## Idee siehe unten, "erhöhe Leistung" Multi Threading, Multi Core. 
    elif "Rechne" in query: #API
        pass

    ## Sehr komplex. i.v.m. Frontend Grafisch als transparenter App wie JAVIS. siehe 
    # https://youtu.be/BEw5EFqCCEI?si=o6unXtt8HuubkOK4&t=1045
    # https://www.youtube.com/shorts/XKywZm9lPY8
    # https://www.youtube.com/watch?v=dHZqi6JUBOI&list=LL&index=1
    elif "Kopiere es hier hin" in query: # wäre ein sehr nützlicher Usecase und extrem gut. Deutlich über dem Tellerrand
        pass

## Sage wenn eine Funktion ausfällt.
## Aufgabe mit Rechnenleistung / Leistung erhöhen. Sagen wie viel zur Verfügung. Wie weit erhöht.
## Sage suche erst im lokalen Speicher. Sage wenn nichts gefunden. Sage stelle Verbindung zur API her. Sage wenn Fehler "Kann nicht auf Mainframe zugreifen"
## Frage welche Stadt man das Wetter wissen möchte. Gebe informationen dazu. Möglichkeit mehr Information dazu abzurufen. Frage was man genau wissen möchte. Gebe Antowrt was man alles bereitsstellen kann.
## Höre zu und antworte wenn ich den Namen rufe.
## Sage wenn eine Funktion ausfällt.

    
