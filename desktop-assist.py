import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib



engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!!")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    speak("I am Ajay's bot .how may I help you ?")

#takes input from microphone and returns string
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print('recognizing...')
        query=r.recognize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print('say that again...')
        return None
    return query

def sendEmail(to, content):
     



    
if __name__ == "__main__":
    wishme()
    while True:
        query=takecommand().lower()
        # logic for exceution task
        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query=query.replace('wikipedia',"")
            results=wikipedia.summary(query,sentences=2)
            speak('According to wikipedia')
            print(results)
            speak(results)
        
        elif ' openyoutube ' in query:
            webbrowser.open('youtube.com')
        
        elif ' opengoogle ' in query:
            webbrowser.open('google.com')
        
        elif 'play music' in query:
            music_dir='C:\\Users\\ajayp\\Music'
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {speak(strtime)}")

        elif 'open code' in query:
            code_dir="C:\Users\ajayp\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(code_dir)

        elif 'send email' in query:
            try:
                speak('what should is say')
                cotent=takecommand()
                to='ajaypatel.te19@bmsce.ac.in'
                sendEmail(to, content)
                speak('email has been send')
            except Exception as e:
                print(e)
                speak("sorry couldnt send")