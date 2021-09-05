from pyfirmata import *

import time
def think():
	placa = Arduino("/dev/ttyACM0")
	for i in range(5):
		placa.digital[13].write(1);
		time.sleep(1)
		placa.digital[13].write(0);
		time.sleep(1)
think()
