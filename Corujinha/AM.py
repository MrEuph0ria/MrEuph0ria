#DEUS É BOM O TEMPO TODO E O TEMPO TODO DEUS É BOM
#CORUJINHA IS THE BEST
#DEV MR.EuPh0ria
#AQUI NÓS É PAMPA E O RESTO É PAMFAS
from pyfirmata import *
from time import *
def finger():
	port = ("/dev/ttyACM0")

	pin = 8

	placa = Arduino(port)

	placa.digital[pin].mode = SERVO

	def rotateServo(pin, angle):
		placa.digital[pin].write(angle)
		sleep(0.015)
	print("pão")
	print("pampas")
	for i in range(0,100):
		rotateServo(pin, i)
	for i in range(180,1,-1):
		rotateServo(pin, i)
		print(i)
	print("cabou o pão")
	#while True:
finger()
