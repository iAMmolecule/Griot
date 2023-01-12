
#import necessary libraries 
import speech_recognition as sr
import os
from time import ctime
import time
import warnings

#suppress any warning messages
warnings.filterwarnings("ignore")

#record sound from microphone
def sound_record():
    r = sr.Recognizer()
    with sr.Microphone() as source:
    	audio = r.listen(source)
data = ""

    #attempt to recognize the spoken words
def recognize_audio(audio):
    try: 
        data = r.recognize_google(audio)
        print("You said: "+ data)
    except sr.UnknownValueError:
        print("I could not understand audio")
    except sr.RequestError:
        print("Network Error")
    return data

result  = recognize_audio(audio)

#receive commands and execute action
def assistant(data):
	if ("what time is it" in data):
		print(ctime())
	elif ("where is" in data):
		data = data.split(" ")
		location = data[2]
		os.system("open maps",location)
    #execute other commands here:

#begin the voice assistant loop
while(1):
	data = sound_record() 
	assistant(data)