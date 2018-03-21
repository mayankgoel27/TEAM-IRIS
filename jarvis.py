import pyaudio
import speech_recognition as sr
from pygame import mixer
import firebase
import os
import random
import socket
import webbrowser
import subprocess
import glob
from time import localtime, strftime
import speekmodule

doss = os.getcwd()
i=0
n=0
def start():
    message = str(firebase.get('String', None))
    print (message)

    result1 = str(firebase.get('/Output', None))
    while 'On' in result1:
        if ('goodbye') in message:
            rand = "Goodbye Sir', 'iris powering off in 3, 2, 1, 0"
            firebase.put('/', 'RaspberryString',"no text to speak")
        break
            
        if ('hello') in message or ('hi') in message:
            rand = "Wellcome to datrix virtual intelligence project. At your service sir."
            firebase.put('/', 'RaspberryString',"no text to speak")

        if ('thanks') in message or ('tanks') in message or ('thank you') in message:
            rand = "You are wellcome', 'no problem"
            firebase.put('/', 'RaspberryString',"no text to speak")

        if message == ('iris'):
            rand = "Yes Sir?', 'What can I doo for you sir?"
            firebase.put('/', 'RaspberryString',"no text to speak")

        if  ('how are you') in message or ('and you') in message or ('are you okay') in message:
            rand = "Fine thank you"
            firebase.put('/', 'RaspberryString',"no text to speak")

        if  ('*') in message:
            rand = "Be polite please"
            firebase.put('/', 'RaspberryString',"no text to speak")

        if ('google maps') in message:
            query = message
            stopwords = ['google', 'maps']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            Chrome = ("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s")
            webbrowser.get(Chrome).open("https://www.google.be/maps/place/"+result+"/")
            rand = result+"on google maps"
            firebase.put('/', 'RaspberryString',"no text to speak")

        if message != ('start music') and ('start') in message:
            query = message
            stopwords = ['start']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('start ' + result)
            rand = "starting"+result
            firebase.put('/', 'RaspberryString',"no text to speak")

        if message != ('stop music') and ('stop') in message:
            query = message
            stopwords = ['stop']
            querywords = query.split()
            resultwords  = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            os.system('taskkill /im ' + result + '.exe /f')
            rand = "stopping"+result
            firebase.put('/', 'RaspberryString',"no text to speak")

        if ('music') in message:
            mus = random.choice(glob.glob(doss + "\\music" + "\\*.mp3"))
            os.system('chown -R user-id:group-id mus')
            os.system('start ' + mus)
            rand = "start playing"
            firebase.put('/', 'RaspberryString',"no text to speak")

        if ('what time') in message:
            tim = strftime("%X", localtime())
            rand = tim
            firebase.put('/', 'RaspberryString',"no text to speak")


