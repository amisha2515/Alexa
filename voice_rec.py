import speech_recognition as sr
import pyttsx3 
import pywhatkit 
import datetime
import wikipedia
import pyjokes
import webbrowser
import os

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.runAndWait()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            print(command)
    except:
        print("microphone not working")
    
    return command

def run_alexa():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','...')
        talk('pllaying'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        talk('time is '+time)
        print(time)
    elif 'who is' in command:
        person=command.replace("who is","")
        info=wikipedia.summary(person,1)
        
        talk(info)
        print(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'open youtube' in command:
            webbrowser.open('youtube.com')
        
    elif 'open google' in command:
            webbrowser.open('google.com')
    elif 'play music' in command:
            music_dir="C:\\Users\\amish\\Music"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
    elif 'open vs code' in command:
            code_dir="C:\\Users\\amish\\OneDrive\\Desktop\\Visual Studio Code.lnk"
            os.startfile(code_dir)
    
    elif 'bye'in command:
        talk("okay bye bye. see you soon")
        quit()
       
    else:
        talk("please say the command again")

        
while True:
    run_alexa()