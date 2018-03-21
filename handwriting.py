import cv2
import numpy as np
from pygame import mixer
import requests;
import speekmodule;
from firebase import firebase
firebase = firebase.FirebaseApplication('https://iaid1-67729.firebaseio.com', None)
import time
import requests
def read(n):
    camera_port = 1
    camera = cv2.VideoCapture(camera_port)
    def get_image():
        retval,im = camera.read()
        return im
    camera_capture = get_image()
    file = "test_image.png"
    cv2.imwrite(file, camera_capture)
    del(camera)
    subscription_key = "461680fae28245d6a428b49670207d36"
    assert subscription_key
    vision_base_url = "https://westcentralus.api.cognitive.microsoft.com/vision/v1.0/"
    text_recognition_url = vision_base_url + "RecognizeText"
    image_url = "test_image.png"
    image_data = open(image_url, "rb").read()
    headers  = {"Content-Type": "application/octet-stream",'Ocp-Apim-Subscription-Key': subscription_key}
    params   = {'handwriting' : True}
    data     = {'url': image_url}
    response = requests.post(text_recognition_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    operation_url = response.headers["Operation-Location"]
    analysis = {}
    while not "recognitionResult" in analysis:
        response_final = requests.get(response.headers["Operation-Location"], headers=headers)
        analysis       = response_final.json()
        time.sleep(1)
    polygons = [(line["boundingBox"], line["text"]) for line in analysis["recognitionResult"]["lines"]]
    i=0
    result=""
    for all in analysis['recognitionResult']['lines']:
        result+="\n"+analysis['recognitionResult']['lines'][i]['text']
        i=i+1
    print(result)
    n=n+1
    try:
        firebase.put('/', 'RaspberryString', result)
    except:
        firebase.put('/', 'RaspberryString',"no text to speak")




