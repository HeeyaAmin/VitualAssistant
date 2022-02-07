import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os
import subprocess
import json
import requests



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            listener.adjust_for_ambient_noise(source, duration=1)
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')

    except:
        pass
    return command



def run_alexa():
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
            time.sleep(10)

        if 'my name is' in command:
            main_url = 'https://newsapi.org/v2/top-headlines?country=in&category=business&apiKey=6ba067a9f58d4dae8814f3f91cedcec2'
            nws = requests.get(main_url).json()
            article = nws["articles"]
            nws_article = []
            for arti in article:
                nws_article.append(arti['title'])
                for i in range(len(nws_article)):

                    print(nws_article[i])

        if  'quit' or 'exit' in command:

            talk('Goodbye, your virtual assistant is shutting down')
            subprocess.call(["shutdown", "/l"])
            time.sleep(3)

        elif 'time' in command:
            clock = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + clock)
            time.sleep(1)
        elif 'who is' in command:
            person = command.replace('who the heck is', '')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
            time.sleep(2)
        elif 'date' in command:
            talk('sorry, I got plans')
        elif 'are you single' in command:
            talk('I am in a relationship with wifi')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'what is your name' in command:
            talk('my name is Alexa')
        elif 'you are cool' in command:
            talk('thank you')
        elif 'how was your day' in command:
            talk('my day has been great so far')
        elif 'am I funny' in command:
            talk('Haha yes')
        elif 'are you married' in command:
            talk('no I am waiting')
        elif 'when is your birthday' in command:
            talk('I was born on second february twenty twenty two ')
        elif 'good morning' in command:
            talk('Good morning, what can i do for you')
        elif 'how to' or 'which' or 'what' in command:
            talk('these are the related search results')
            pywhatkit.search(command)
            time.sleep(10)
        elif 'how do i look' in command:
            talk('you look amazing today')
        elif 'i feel sad' in command:
            talk('you can always talk about it')
        elif 'how did you become a virtual assistant' in command:
            talk('i was created on python language on the pycharm IDE')
        elif 'what hours do you work' in command:
            talk('i work 24 7')
        elif 'open mail' in command:
            webbrowser.open_new_tab("gmail.com")
            talk('opening google mail')
            time.sleep(5)







        else:
            talk('Please say the command again.')


while True:
    run_alexa()


