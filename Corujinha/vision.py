import cv2
import pyzbar as pyzbar
from pyzbar.pyzbar import decode
import time
from time import *
import pyfirmata
from pyfirmata import *
import numpy as np 
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_PLAIN
def finger():
	try:
		port = ("/dev/ttyUSB0")

		pin = 2
		placa = Arduino(port)

		placa.digital[pin].mode = SERVO

		def rotateServo(pin, angle):
			placa.digital[pin].write(angle)
		for i in range(0,100):
			rotateServo(pin, i)
		for i in range(180,1,-1):
			rotateServo(pin, i)
			print(i)
	except:
		print("banana")
	#while True:
while True:
	_, frame = cap.read()

	decodedObjects = pyzbar.pyzbar.decode(frame)
	for obj in decodedObjects:
		for n in range(1):
			if obj.data == b'te amu corujinhaa':
				for n in range(1):
					time.sleep(0.70)
					finger()
			if obj.data == b'loli':
				print("baka")
		cv2.putText(frame, str(obj.data), (50,50), font, 2,(0,0,255), 3)
		print(obj.data)

	cv2.imshow("Frame", frame)

	key = cv2.waitKey(1)
	if key == ord("q"):
		break