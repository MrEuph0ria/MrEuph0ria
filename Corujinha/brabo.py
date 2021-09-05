import cv2
import time
from time import *
import pygame
from pynput.mouse import Button, Controller
import pyzbar as pyzbar
from pyzbar.pyzbar import decode
from pyfirmata import *
print("2")
print("12")
print("8")
print("10")
servor = int(input("qual servo quer mover?"))
mouse = Controller()
font = cv2.FONT_HERSHEY_PLAIN
try:
    port = ("/dev/ttyUSB0")

    pin = servor
    placa = Arduino(port)

    placa.digital[pin].mode = SERVO

    def rotateServo(pin, angle):
        placa.digital[pin].write(angle)
        sleep(0.015)
        print("pão")
except:
    print("legal")
def olhos():
    cam = cv2.VideoCapture(0)

    while cam.isOpened():
        ret,frame1 = cam.read()
        ret,frame2 = cam.read()
        decodedObjects = pyzbar.pyzbar.decode(frame1)
        for obj in decodedObjects:
            for n in range(1):
                if obj.data == b'te amu corujinhaa':
                    print("legal")
            cv2.putText(frame1, str(obj.data), (100,50), font, 2,(0,0,255), 3)
        diff = cv2.absdiff(frame1, frame2)
        gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
        dilated = cv2.dilate(thresh, None, iterations=3)
        contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        for c in  contours:
            if cv2.contourArea(c) < 5000:
                continue
            x, y , w, h = cv2.boundingRect(c)
            cv2.rectangle(frame1, (x,y), (x + w, y + h), (255,0,0), 2)
            
            mouse_x = ((x+w/2) / 2.214 )+550
            if mouse_x <= 677:
                mouse_x = 90
            if mouse_x >= 677:
                mouse_x = 1

            mouse.position = (mouse_x, 50)
            try:
                rotateServo(pin, mouse_x)
            except:
                print("sem conexões com Arduino")
            #mouse.press(Button.left)

        if cv2.waitKey(10) == ord ("q"):
            break
        cv2.imshow("CAMERA", frame1)

olhos()