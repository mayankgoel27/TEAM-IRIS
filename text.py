import cv2
import numpy as np
from pygame import mixer
import requests;
import speekmodule;
from firebase import firebase
firebase = firebase.FirebaseApplication('https://iaid1-67729.firebaseio.com', None)
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
    ocr_url = vision_base_url + "ocr"
    image_url = "test_image.png"
    image_data = open(image_url, "rb").read()
    headers  = {'Ocp-Apim-Subscription-Key': subscription_key,"Content-Type": "application/octet-stream"}
    params   = {'language': 'unk', 'detectOrientation ': 'true'}
    data1     = {'url': image_url}
    response = requests.post(ocr_url, headers=headers, params=params, data=image_data)
    response.raise_for_status()
    analysis = response.json()
    line_infos = [region["lines"] for region in analysis["regions"]]
    word_infos = []
    for line in line_infos:
        for word_metadata in line:
            for word_info in word_metadata["words"]:
                word_infos.append(word_info)
    word_infos
    i=0;
    result=""
    for all in word_infos:
        print(word_infos[i]['text'])
        result+=" "+word_infos[i]['text']
        i=i+1
    print(result)
    if(result==""):
        result = "no text to speak"
        firebase.put('/', 'RaspberryString', result)
    else:
        firebase.put('/', 'RaspberryString', result)
