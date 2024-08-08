from playsound import playsound

import eel
from engine.command import speak
import os
from engine.config import ASSISTANT_NAME



#playing assistant sound function


@eel.expose

def playAssistantSound():
    music_dir = "www\\assests\\audio\\music effect2.mp3"
    playsound(music_dir)


def openCommand(query): 
    query = query.replace(ASSISTANT_NAME, "")

    query = query.replace("open", "")

    query.lower()

    if query!="":
          speak("Opening "+query)
          os.system('start'+query)

    else:
          speak("not found")


def PlayYoutube(query):
    search_term = extract_yt_term(query)
    speak("Playing "+search_term+" on YouTube")
    kit.playonyt(search_term)          
  