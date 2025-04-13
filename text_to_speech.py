import re
import time
from icecream import ic
from settings import settings
import edge_tts #pip install edge_tts


def remove_asterisks(welcometext):
    #Entfernt alle Sternchen (*) und (-) aus dem GPT content.
    # return: String ohne * und -
    return re.sub(r'[\*-]', '', welcometext)

## async ist eine besondere Funktion. Asynchrones Programmieren. Nicht so wie das Normale synchrone was codezeile nach codezeile in einer Abfolge abarbeitet. Hier braucht man auch besondere Syntax, async und await. async initialisiert und await lässt der Code an der stelle stehen und es werden keine neuen Ressourcen freigeben. Ist fortgeschrittnes Python programmieren braucht man aber hier. Threding hilfreich zu verstehen um das zu verstehen.
async def text_to_mp3(welcometext,filename,voice,rate,pitch):
    communicate = edge_tts.Communicate(welcometext, voice, rate=rate, pitch=pitch)
    await communicate.save(settings.filename)  ## warte bis file gespeichert bevor codezeile verlassen wird.
    #print(f"Saved {filename}")
