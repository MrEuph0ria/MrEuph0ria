from random import *
import random
import time
def jokenpo():
    escolhas = ["pedra", "papel", "tesoura"]
    ran = random.randint(0,2)
    print("pedra")
    time.sleep(3)
    print("papel")
    time.sleep(3)
    print("tesoura")
    time.sleep(2)
    print(escolhas[ran])
jokenpo()