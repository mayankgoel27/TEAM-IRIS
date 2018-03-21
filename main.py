from firebase import firebase
import time
import analyze
import text
import handwriting
import jarvis
firebase = firebase.FirebaseApplication('https://iaid1-67729.firebaseio.com', None)
n=0
result1 = str(firebase.get('/Output', None))
while 1:
    while 'On' in result1:
        result1 = str(firebase.get('/Output', None))
        n=n+1
        result = str(firebase.get('/String', None))
        print (result)
        if('see') in result or ('analyse') in result or ('describe') in result:
            analyze.read(n)
        if('read') in result or ("this text") in result or ('read this') in result:
          text.read(n)
        if('hand writting') in result or ('hand') in result or ('written') in result:
          handwriting.read(n)
        if('Assist me') in result:
         jarvis.start()
