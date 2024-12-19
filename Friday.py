import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import time
from groq import Groq

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}\n")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return None
    except sr.RequestError:
        speak("Could not request results from Google Speech Recognition service; check your internet connection.")
        return None

def get_pentestgpt_response(query):
    client = Groq(
        api_key="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",
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": "You are friday, an AI assistant created by  pratyoosh shukla,Pratyoosh Shukla is a talented 7th-grader from Mumbai, passionate about coding and experimenting with Arduino-based projects, while also excelling as a wicket-keeper in cricket.",
            },
            {
                "role": "user",
                "content": query,
            }
        ],
        model="llama3-8b-8192",
    )

    return chat_completion.choices[0].message.content

def respond_to_query(query):
    if "open youtube" in query:
        speak("Opening YouTube.")
        webbrowser.open("https://www.youtube.com")
    elif "open twitter" in query:
        speak("Opening Twitter.")
        webbrowser.open("https://www.twitter.com")
    elif "open instagram" in query:
        speak("Opening Instagram.")
        webbrowser.open("https://www.instagram.com")
    else:
        pentestgpt_response = get_pentestgpt_response(query)
        speak(pentestgpt_response)

def main():
    speak("Hello! I am your AI voice assistant. How can I help you?")
    while True:
        query = listen()
        if query:
            respond_to_query(query)

if __name__ == "__main__":
    main()