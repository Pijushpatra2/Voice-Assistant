import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty("rate" ,180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
      
def greetMe():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        speak('Good Morning Boss')
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"sir, the time is {strTime}")
    elif hour>12 and hour<=18:
        speak('Good Afternoon Boss')
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"sir, the time is {strTime}")
    else:
        speak('Good Evening Boss')
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"sir, the time is {strTime}")


