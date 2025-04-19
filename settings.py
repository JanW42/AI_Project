from dataclasses import dataclass

@dataclass
class settings:
    ## Edge_tts text_to_speech
    welcometext = "Hallo mein Name ist Alessa. Wie kann ich dir helfen?"
    #welcometext = "Elon Musk ist ein in Südafrika geborener Unternehmer und Milliardär, der für seine Beteiligung an mehreren bahnbrechenden Technologieunternehmen bekannt ist. Er wurde am 28. Juni 1971 in Pretoria, Südafrika, geboren. Hier sind einige der wichtigsten Aspekte seines Lebens und seiner Karriere: 1. Frühes Leben und Bildung: Musks Interesse an Technologie und Computern begann in seiner Kindheit. Er zog im Alter von 17 Jahren nach Kanada und besuchte die Queen's University in Ontario, bevor er zur University of Pennsylvania wechselte, wo er zwei Abschlüsse in Physik und Wirtschaft erwarb. 2. Frühe unternehmerische Aktivitäten: Musk gründete in den 1990er Jahren sein erstes Unternehmen, Zip2, eine OnlineStadtführerSoftware für Zeitungen. Zip2 wurde 1999 für fast 300 Millionen Dollar verkauft. 3. PayPal: Nach dem Verkauf von Zip2 gründete Musk X.com, ein OnlineZahlungssystem. Dieses Unternehmen fusionierte später mit Confinity und wurde zu PayPal, das 2002 von eBay für 1,5 Milliarden Dollar in Aktien gekauft wurde. 4. SpaceX. 2002 gründete Musk Space Exploration Technologies Corp. oder SpaceX, mit dem Ziel, die Raumfahrt kostengünstiger und zugänglicher zu machen. SpaceX hat bedeutende Erfolge erzielt, darunter die Entwicklung der FalconRaketen und der DragonRaumkapsel sowie die Landung und Wiederverwendung von Raketenbooster. Das ultimative Ziel von SpaceX ist die Kolonisierung des Mars. 5. Tesla, Inc.: 2004 trat Musk dem von Martin Eberhard und Marc Tarpenning gegründeten Unternehmen Tesla Motors (später Tesla, Inc.) bei und leitete die erste Investitionsrunde. Tesla ist heute ein führender Hersteller von Elektrofahrzeugen und Energiespeicherlösungen. Unter Musks Führung hat Tesla Modelle wie den Model S, Model 3, Model X und Model Y entwickelt und produziert. 6. Weitere Unternehmen: SolarCity: Musk war Mitbegründer von SolarCity, einem Anbieter von Solaranlagen, der später von Tesla übernommen wurde. The Boring Company: Dieses Unternehmen wurde gegründet, um Tunnelbau und Infrastrukturlösungen zu entwickeln. Es hat Projekte wie den Bau eines Tunnelsystems zur Reduzierung des Verkehrs in städtischen Gebieten initiiert. Neuralink: Musk gründete Neuralink, ein Unternehmen, das Technologien zur Verbindung des menschlichen Gehirns mit Computern entwickelt, um neurologische Probleme zu behandeln und die menschliche Leistungsfähigkeit zu steigern. OpenAI: Er war ein Mitbegründer von OpenAI, einer Forschungseinrichtung, die das Ziel verfolgt, künstliche Intelligenz sicher und nützlich zu gestalten. 7. Persönliches Leben: Musk war mehrfach verheiratet und hat mehrere Kinder. Er ist für seine intensive Arbeitsethik bekannt und verbringt oft viel Zeit in seinen verschiedenen Unternehmen. Musk ist auch für seine öffentliche Präsenz auf SocialMediaPlattformen, insbesondere Twitter, bekannt, wo er häufig seine Meinungen und Unternehmensankündigungen teilt. Elon Musk hat durch seine vielfältigen Aktivitäten und Visionen maßgeblich zur technologischen Entwicklung in verschiedenen Branchen beigetragen. Er wird als einer der einflussreichsten Technologen und Unternehmer der Gegenwart betrachtet."
    
    filename  = "output.mp3"    #zu wav datei machen!!! mehr performance
    voice = "de-DE-SeraphinaMultilingualNeural"
    rate="+10%"
    pitch="+10Hz"

    ## GPT API
    model = "gpt4o"
    # GPT Model Dic
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
 
    ## faster_whisper speech_to_text
    model_size = "medium"  #large-v3 #medium
    # Run on GPU with FP16
    device="cuda"
    compute_type="float16"
    # model = WhisperModel(model_size, device="cuda", compute_type="float16")
    # or run on GPU with INT8
    # model = WhisperModel(model_size, device="cuda", compute_type="int8_float16")
    # or run on CPU with INT8
    # model = WhisperModel(model_size, device="cpu", compute_type="int8")