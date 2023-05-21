import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import wolframalpha
import pygame
import pyjokes
import os

listener = sr.Recognizer()
engine = pyttsx3.init()
client = wolframalpha.Client("KJWJ99-K3TR6275WV")
pygame.init()

def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'assistant' in command:
                command = command.replace('assistant', '')
                print(command)
    except:
        pass
    return command

def run_assistant():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)
    elif 'search' in command:
        search_term = command.replace('search', '')
        talk('Searching for ' + search_term)
        pywhatkit.search(search_term)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('The time is ' + time)
    elif 'date' in command:
        date = datetime.datetime.now().strftime('%B %d, %Y')
        talk('Today is ' + date)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
    elif 'calculate' in command:
        query = command.replace('calculate', '')
        try:
            res = client.query(query)
            answer = next(res.results).text
            talk("The answer is " + answer)
        except:
            talk("Sorry, I couldn't find an answer for that")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'game' in command:
        talk('Opening game')
        os.system('start chrome.exe https://www.google.com/doodles/celebrating-the-50th-anniversary-of-logical-operators')
    elif 'stop' in command:
        pygame.mixer.music.stop()
    elif 'play music' in command:
        music_dir = 'C:/Music'
        songs = os.listdir(music_dir)
        song = os.path.join(music_dir, songs[0])
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
    else:
        talk('Please say the command again.')

while True:
    run_assistant()
