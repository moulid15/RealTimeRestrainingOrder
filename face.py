import cv2
import time
import sys
from serial import Serial
import numpy as np

#/****************************************************/
#/* Name of the project:Real-time restraining order  */
#/* Author:Moulid Ahmed     	                    */
#/* 		-Any other info-                        */
#/* Date : 11/22/2019                              */
#/*************************************************/

#first attempt to test arduino and face recongition
arduino = Serial('/dev/ttyACM0',9600)
time.sleep(2)
print('connecting to arduino')

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#To capture the video stream from webcam.
cap = cv2.VideoCapture(0)
#Read the captured image, convert it to Gray image and find faces
while 1:
    ret, img = cap.read()
    # cv2.resizeWindow('img', 500,500)
    cv2.line(img,(500,250),(0,250),(0,255,0),1)
    cv2.line(img,(250,0),(250,500),(0,255,0),1)
    cv2.circle(img, (250, 250), 5, (255, 255, 255), -1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3)
#detect the face and make a rectangle around it.
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),5)
        roi_gray  = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        arr = {y:y+h, x:x+w}
        print (arr)

        print ('X :' +str(x))
        print ('Y :'+str(y))
        print ('x+w :' +str(x+w))
        print ('y+h :' +str(y+h))
# Center of Rectangle
        xx = int(x+(x+h))/2
        yy = int(y+(y+w))/2
        print (xx)
        print (yy)
        center = (xx,yy)
# sending data to arduino
        print("Center of Rectangle is :", center)
        data = "X{0:f}Y{1:f}Z".format(xx, yy)
        print ("output = '" +data+ "'")
        arduino.write(data.encode())
#Display the stream.
    cv2.imshow('img',img)
#Hit 'Esc' to terminate execution
    k = cv2.waitKey(30) & 0xff
    if k == 27:
       break
