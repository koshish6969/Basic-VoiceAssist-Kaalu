import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os 

engine = pyttsx3.init ('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Koshish")
    elif hour>12 and hour<18:
        speak("Good Afternoon Koshish")
    else:
        speak("Good Evening Koshish")
    
    speak("I am Kaalu. How may I help you?")

def takeCommand():
    #It takes microphone input from the user and returns string output
    #creating recognizer object
    r = sr.Recognizer()
    #Capture audio from the default microphone
    with sr.Microphone() as source:
        print("Kaalu is Listening....")
        #creating pause threshold to 1 second
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio)
        print(f"User said:{query}\n")


    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
    wishMe()
    while True:
       query=takeCommand().lower()

    #Logic for executing tasks that is based on query
       if 'wikipedia' in query:
           speak("Searching Wikipedia...")   
           query=query.replace("wikipedia","")
           results=wikipedia.summary(query,sentences=2) 
           speak("According to Wikipedia")
           print(results)
           speak(results)
        
       elif 'open youtube' in query:
           webbrowser.open("https://www.youtube.com/")
           
       elif 'open google' in query:
           webbrowser.open("https://www.google.com/")

       
       elif 'play any music' in query:
           music_dir='D:\\mewsic'
           songs=os.listdir(music_dir)
           print(songs)
           os.startfile(os.path.join(music_dir,songs[0]))

       elif 'current time' in query:
           strTime=datetime.datetime.now().strftime("%H:%M:%S")
           speak(f"The current time is {strTime}")
        
       elif 'open code' in query:
           CodePath = "C:\Users\\Koshish Shrestha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
           os.startfile(CodePath)

        