import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query
speak("Hey User")
query = takeCommand().lower()
if "Hey, Nova" in query:
    if __name__ == "__main__":
        while True:
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            elif 'open youtube' in query:
                webbrowser.open("youtube.com")

            elif "play" in query:
                query.replace("play")
                webbrowser.open(f'youtube.com/results?search_query={query}')

            elif "search" in query:
                query.replace('search')
                webbrowser.open(f"www.google.com/search?q={query}")
            elif 'open google' in query:
                webbrowser.open("google.com")
            elif 'open stackoverflow' in query:
                webbrowser.open("stackoverflow.com")
            elif "toss a coin for me" in query:
                x = random.choice(0,1)
                if x == 0:
                    speak("Head")
                elif x==1:
                    speak("Tail")
            elif "Tell me a joke" in query:
                
                speak()

            elif 'bye' in query:
                speak("Okay! Bye")
                break