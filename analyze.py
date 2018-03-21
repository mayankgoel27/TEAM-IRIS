from firebase import firebase
firebase = firebase.FirebaseApplication('https://iaid1-67729.firebaseio.com', None)
import cv2
import numpy as np
from pygame import mixer
import requests;
import speekmodule;

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
    vision_analyze_url = vision_base_url + "analyze"
    image_path = "test_image.png"
    import requests
    image_data = open(image_path, "rb").read()
    headers    = {'Ocp-Apim-Subscription-Key': subscription_key,"Content-Type": "application/octet-stream" }
    params        = {'visualFeatures': 'Categories,Description,Color'}
    response   = requests.post(vision_analyze_url, 
                               headers=headers, 
                               params=params, 
                               data=image_data)

    response.raise_for_status()
    analysis      = response.json()
    image_caption = analysis["description"]["captions"][0]["text"].capitalize()
    image_caption
    print(image_caption)                        
    firebase.put('/','RaspberryString',image_caption)
