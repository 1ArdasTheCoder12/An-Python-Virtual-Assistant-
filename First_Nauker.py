import pyttsx3
import webbrowser
import musicLibrary
import speech_recognition as sr
import requests
from openai import OpenAI
import pygame
from gtts import gTTS
import time
import os
import uuid
# Initialize the speech engine
engine = pyttsx3.init()
# List available voices
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Example: Zira (female)

# Set rate (words per minute)
engine.setProperty('rate', 150)  # 125–175 sounds clearer

# Set volume
engine.setProperty('volume', 1.0)

# News API key
newsapi = "87deca848c3e4c22b1ddb9c97726e614"

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()
#gtts    
# AI response processing
def Aiproccess(command):   
    client = OpenAI(api_key="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")
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        store=True,
        messages=[
            {
                "role": "system",
                "content": "HELLO I AM JARVIS, I AM A VIRTUAL ASSISTANT THAT HELPS MAKE TASKS EASY LIKE OPENING YOUTUBE, WHATSAPP, PLAYING SONGS. I AM MADE BY THE GENIUS CODER ARDAS TIWARI."
            },
            {"role": "user", "content": command}
        ]
    )
    return completion.choices[0].message.content  # ✅ Fixed return

# Command processor
def processCommand(command):
    print("Command:", command)
    command = command.lower().replace("jarvis", "").strip()

    if "open youtube" in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif command.startswith("play"):
        parts = command.split(" ", 1)
        if len(parts) > 1:
            song = parts[1]
            try:
                speak(f"Playing {song}")
                musicLibrary.play(song)
            except KeyError:
                speak(f"Sorry, I don’t have '{song}' in my library.")
        else:
            speak("Please tell me which song to play.")

    elif "news" in command:
        r = requests.get(f"https://newsapi.org/v2/everything?q=Apple&from=2025-04-29&sortBy=popularity&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])
    else:
        output = Aiproccess(command)
        print("AI:", output)
        speak(output)

# Main program loop
if __name__ == "__main__":
    speak("Installing Jarvis")
    jarvis_active = False
    recognizer = sr.Recognizer()

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                recognizer.adjust_for_ambient_noise(source, duration=0.5)
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                recognized_text = recognizer.recognize_google(audio)
                print(f"Command: {recognized_text}")
                
                if "jarvis" in recognized_text.lower():
                    speak("Yes sir!")
                    print("Jarvis is Activated!")
                    jarvis_active = True
                elif jarvis_active:
                    processCommand(recognized_text)

        except sr.WaitTimeoutError:
            print("Listening timed out. Try again.")
        except sr.UnknownValueError:
            print("Could not understand audio.")
        except sr.RequestError as e:
            print(f"Speech Recognition error: {e}")



























































































































































































































































