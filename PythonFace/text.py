from playsound import playsound
from gtts import gTTS
import os
tts = gTTS(text='Just say hey google get me digital death planner on the phone kept next to me', lang='en')
tts.save("close.mp3")
playsound('close.mp3')


# from playsound import playsound
# playsound('audio.mp3')