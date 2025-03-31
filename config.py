from dataclasses import dataclass

@dataclass
class config:

    AZURE_OPENAI_API_KEY = "d1b978271d584026b6e4e3a8083dbc9b"
    AZURE_OPENAI_ENDPOINT = "https://bueckermsgpt4.openai.azure.com/"
    OPENAI_API_VERSION = "2024-02-15-preview"

    WEATHER_API_KEY = "6357cf0fb5accf3932386e26833a37c7"

    # Ideen
    '''
    JAVIS/Friday mit Grafischer Operfläche.. Animation mit Code oder Text der im Hintergrund durchläuft. Dazu Darkmode und Wenn reden dann ändert sich die Grafik
    Fragen beantworten über GPT oder Weather API oder Finance API
    Bilder generieren von Dingen
    Spiele Musik
    Wichtige Nachrichten
    Was ist an der Börse los / Zeitungen analysieren

    Vllt Transparentes Fenster unten in der Ecke und dann kann man Ergebnisse zum Beispiel Code direkt an den Curser rein Kopieren
    
    pip install playsound == 1.2.2

    '''