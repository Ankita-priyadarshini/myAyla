import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_sphinx(voice)
            print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    print(command)
    # if 'play' in command:
    song = command.replace('play', '')
    talk('playing ' + song)
    pywhatkit.playonyt(song)
    # elif 'time' in command:
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('Current time is ' + time)
    # elif 'wikipedia' in command:
    data = command.replace('wikipedia', '')
    info = wikipedia.summary(data, 4)
    print(info)
    talk('data')
    # elif 'joke' in command:
    talk(pyjokes.get_joke())
    # else:
    talk('Sorry I did not understand. Please try again.')

while True:
    run_alexa()
