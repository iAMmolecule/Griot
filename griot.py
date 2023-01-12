# Importing necessary libraries 
import speech_recognition as sr 
import pyttsx3 
import datetime 
import wikipedia 
import webbrowser
import os 

# Initializing the speech engine 
engine = pyttsx3.init('sapi5') 
voices = engine.getProperty('voices') 
# Changing the voice 
engine.setProperty('voice', voices[0].id) 

# Function to speak 
def speak(audio): 
	engine.say(audio) 
	engine.runAndWait() 

# Function to wish me 
def wishMe(): 
	hour = int(datetime.datetime.now().hour) 
	if hour>=0 and hour<12: 
		speak("Good Morning!") 

	elif hour>=12 and hour<18: 
		speak("Good Afternoon!") 

	else: 
		speak("Good Evening!") 

	speak("I am your assistant. Please tell me how may I help you") 

# Function to take command 
def takeCommand(): 
	# It takes microphone input from user and returns string output 
	r = sr.Recognizer() 
	with sr.Microphone() as source: 
		print("Listening...") 
		r.pause_threshold = 1
		audio = r.listen(source) 

	try: 
		print("Recognizing...") 
		query = r.recognize_google(audio, language ='en-in') 
		print(f"User said: {query}\n") 

	except Exception as e: 
		# print(e) 
		print("Say that again please...") 
		return "None"
	return query 

if __name__ == "__main__": 
	wishMe() 
	# while True: 
	if 1: 
		query = takeCommand().lower() 

		# Logic for executing tasks based on query 
		if 'wikipedia' in query: 
			speak('Searching Wikipedia...') 
			query = query.replace("wikipedia", "") 
			results = wikipedia.summary(query, sentences = 2) 
			speak("According to Wikipedia") 
			print(results) 
			speak(results) 

		elif 'open youtube' in query: 
			webbrowser.open("youtube.com") 

		elif 'open google' in query: 
			webbrowser.open("google.com") 

		elif 'open stackoverflow' in query: 
			webbrowser.open("stackoverflow.com")