import pyttsx3
import speech_recognition as sr
import pywhatkit
import wikipedia
import webbrowser

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
        

query = takeCommand()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate" ,180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def searchGoogle(query):  
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("jarvis","")
        query = query.replace("google search","")
        query = query.replace("google","")
        speak("This is what I found on google")
    
    try:
        pywhatkit.search(query)
        result = googleScrap.summery(query,1)
        speak(result)
        
    except:
        speak("sorry sir no output available")
        
def searchYoutube(query):
    if "youtube" in query:
        speak("this is i found sir")
        query = query.replace("jarvis","")
        query = query.replace("youtube search","")
        query = query.replace("youtube","")
        web = "https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done, sir")


def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query = query.replace("jarvis","")
        query = query.replace("search wikipedia","")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 1)
        speak("According to wikipedia...")
        print(results)
        speak(results)

