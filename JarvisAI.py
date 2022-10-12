from time import time
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            #print ("command")
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                time = datetime.datetime.now().strftime('%I:%M %p')
                talk ('Sir, You have no event today and local time is' +time)

    except:
        pass
    return command


def run_jarvis():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'facebook' in command:
        talk('Opening facebook.')
        webbrowser.open('https://www.facebook.com/')
    elif 'email' in command:
        talk('Opening mail.')
        webbrowser.open('https://mail.google.com/')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Wrong voice command.')


while True:
    run_jarvis()




# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                                                   #
#   Disclaimer  : This code is only for educational purposes. And this Jarvis AI is a prototype project.            #
#               It does not pirate anyone's copyright.                                                              #
#   Developper  : Faysal Mahmud                                                                                     #
#   ©Copyright  : Used fot educaton purpose ©Copyright/user                                                         #
#                                                                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #