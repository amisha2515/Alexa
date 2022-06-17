import speech_recognition as sr
import pyttsx3 
import pywhatkit 
import datetime
import wikipedia
import pyjokes

listener=sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
#engine.say('I am ajay bot. How can I help You')
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
    elif 'bye'in command:
        quit
    else:
        talk("please say the command again")

        
while True:
    run_alexa()
            