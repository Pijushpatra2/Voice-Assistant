import pyttsx3
import speech_recognition as sr
import requests
from bs4 import BeautifulSoup
import datetime
import webbrowser


myName = 'jarvis'

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate" ,180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 200
        audio = r.listen(source,0,4)
    try:
        print('Recognizing....')
        query = r.recognize_google(audio, language='en-in')
        print('you said: ', query)
    except Exception:
        print('say that again')
        return 'None'
    return query



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "jarvis" in query:
            from GreetMe import greetMe
            greetMe()

        elif "jarvis are you there" in query:
            speak("yes sir i am always with you")
        elif "what's your full name" in query:
            speak("it's Just A Really Very Intelligent System, sir")  
        elif "How is it" in query:
            speak("As always sir, a greate pleasure watching you work")   
        elif "how are you" in query:
            speak("i am perfact sir, how are you")
        elif "i am fine" in query:
            speak("that's great sir")
        elif "hay jarvis" in query:
            speak("I am Listening")
        elif "thank you" in query:
            speak("you are wellcome, sir")
        elif "jarvis are you up" in query:
            speak("For your sir always")
        elif "how old are you" in query:
            speak("i am still updating, sir")
        
        # for app
        
        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)
        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)
        # search web browser
        
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
        
                            

        elif "today's temperature" in query:
            search = "temperature"
            url = f"https://www.google.com/search?q={search}"
            r = requests.get(url)
            data = BeautifulSoup(r.text, "html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
            
        elif "what's the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"sir, the time is {strTime}")
        elif "go to sleep" in query:
            speak("By sir, take care")
            exit()
            
            
            
    
        
            
