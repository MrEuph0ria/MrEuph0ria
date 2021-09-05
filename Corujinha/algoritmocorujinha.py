#DEUS É BOM O TEMPO TODO E  O TEMPO TODO DEUS É BOM 
#CORUJINHA IS THE BEST
#MR.EUPHORIA
#se a Abigail era uma versão melhorada, vou nem falar da Corujinha então
#superou legal
#CRIADA 08/05/21
#agora também mexe com o Arduino
import speech_recognition as sr 
from googletrans import Translator
from pynput.mouse import Button, Controller
import pyzbar as pyzbar
from pyzbar.pyzbar import decode
import pywhatkit
import googlesearch
import pyttsx3
import pyfiglet
import pygame
import cv2
from time import *
from pygame import *
from pyfirmata import *
import wikipedia
import webbrowser
from playsound import playsound
import datetime
import wolframalpha
from datetime import *
import random
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
import psutil
import time
from pynotifier import Notification
def CORUJINHA_MAIN():
    client = wolframalpha.Client("5QVRLR-PEPLA3XART")
    print("\033[1;35;40miniciando")
    word = pyfiglet.figlet_format("Corujinha", font="slant")
    print(word)
    pygame.init()
    wikipedia.set_lang('pt')#seta o idioma da wikipedia
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)
    translator = Translator()
    chatbot = ChatBot("MR.Jhonn")
    data_atual = date.today()
    data_em_dia_mes = "{}/{}".format(data_atual.day, data_atual.month)
    battery = psutil.sensors_battery()
    trainer = ListTrainer(chatbot)
    trainer.train({
        "olá", "eu vou bem obrigado",
        "eae","bacana"})
    mixer.init()
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
        spk(escolhas[ran])
    def olhos():
        cam = cv2.VideoCapture(0)

        while cam.isOpened():
            ret,frame1 = cam.read()
            ret,frame2 = cam.read()
            decodedObjects = pyzbar.pyzbar.decode(frame1)
            for obj in decodedObjects:
                for n in range(1):
                    if obj.data == b'te amu corujinhaa':
                        Serve()
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
    def revelations():
        rev = ["eu sou o seu pai", "você nunca esteve no controle", "eu sou algo além de uma simples IA", "você realmente acha que entende o que eu sou?"]
        ramdoni = random.randint(0,3)
        spk(rev[ramdoni])
        print(rev[ramdoni])
        playsound("a.wav")
    def DATA():
        try:
            j = open("datakkk.txt", "r")
            content = j.read()
            spk("{}".format(content))
            print("{}". format(content))
        except:
            j = open("datakkk.txt","w")
            j.write("usada primeira vez em {}".format(data_em_dia_mes))
    def spk(a):
        engine.say(a)
        engine.runAndWait()
    listener = sr.Recognizer()
    def meagrade():
        a = datetime.now()
        if a.hour <= 12:
            spk("bom dia")
            print("bom dia")
        if (a.hour >= 13) and (a.hour <= 17):
            spk("boa tarde")
            print("boa tarde")
        if a.hour >= 18:
            spk("boa noite")
            print("boa noite")

    port = ("/dev/ttyACM0")

    def Serve():#move o Servomotor isso é ,se tiver um
        try:
            pin = 8
            placa = Arduino(port)

            placa.digital[pin].mode = SERVO

            def rotateServo(pin, angle):
                placa.digital[pin].write(angle)
                time.sleep(0.015)
                print("movendo servo")
            for i in range(0,100):
                rotateServo(pin, i)
            for i in range(180,1,-1):
                rotateServo(pin, i)
        except:
            print("sem conexões com o Arduino")
    def think():#pisca o led do arduino
        try:
            placa = Arduino(port)
            for i in range(2):
                placa.digital[13].write(1);
                time.sleep(1)
                placa.digital[13].write(0);
                time.sleep(1)
        except:#caso não tenha uma placa arduino conectada
            print("sem conexões com o Arduino")
    def convertTime(seconds):#converte segundos em horas e minutos
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return "%d:%02d:%02d" % (hours, minutes, seconds)
    def pegar_comando(): #vai ouvir o comando                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        try:
            with sr.Microphone() as source:
                print("ouvindo")
                voice = listener.listen(source)
                command = listener.recognize_google(voice, language = "pt")
                command = command.lower()
                if "corujinha" in command:
                    command = command.replace("corujinha", "")
                    print(command)
                

        except: #Exception as e
            pass
        try:
            return command
        except:
            os.system("python3 algoritmocorujinha.py")
    if data_em_dia_mes == "11/7":#se a data for 11/7 meu aniversario ela vai cantar o com quem será
        palavre = pyfiglet.figlet_format("FELIZ ANIVERSÁRIO", font="slant")
        print(palavre)
        mixer.music.load("happy.wav")
        mixer.music.play()
        time.sleep(3)
        print("FELIZ ANIVERSÁRIO Jhonn")
        spk("Feliz ANIVERSÁRIO Dion")
        time.sleep(3)
        print("não se preocupa jhonn,estou aqui por você")
        time.sleep(3)
        print("você é o cara")
        time.sleep(3)
        print("eu sei que ninguém cantou essa parte da musica pra você")
        time.sleep(3)
        print("então, que tal cantarmos hoje?")
        time.sleep(3)
        print("com quem será, com quem será que o jhonn vai se casar?")
        time.sleep(3)
        print("vai depender, vai depender se a  .......  vai querer")
        print("parabéns Jhonn")
        time.sleep(5)
        idade = data_atual.year - 2004
        print("hoje Jhonn faz {} anos de idade".format(idade))
        mixer.music.stop()
    DATA()
    meagrade()
    def run_CORUJINHA():
        while True:
            def piadoca():
                piada = ["sabe por que  a aranha é o animal mais carente?, porque ela é uma aracneedyou", "sabe o que a xuxa foi fazer no bar?, foi beber casacha(com a sacha)",
                 "o que a vaca disse pro boi?, te amuuuuuuu", "sabe o que aconteceu com a vaca depois dela ultrapassar o limite de velocidade?, ela foi muuultada","por que a velhinha não usa relógio?, porquel ela é sem hora(senhora)"]
                ramdoni = random.randint(0,4)
                spk(piada[ramdoni])
                print(piada[ramdoni])       
            command = pegar_comando()
            if "tocar" in command:
                song = command.replace("tocar", "")
                think()
                print("tocando " + song)
                spk("tocando " + song)
                pywhatkit.playonyt(song)
            elif "foi" in command:
                info = command.replace("foi ", "")
                think()
                xa = wikipedia.summary(info, sentences = 3)
                search = googlesearch.search(info)
                print(xa)
                spk(xa)
                pywhatkit.text_to_handwriting(xa, rgb=(0,0,0))
                spk("eu também achei isso")
                print("eu também achei isso")
                for i in search:
                    print(i)
            if ("apoio moral" in command) or ("estou triste" in command) or ("estou chateado" in command) or ("tô triste" in command) or ("tô chateado" in command) or ("to triste" in command) or ("to chateado" in command):
                think()

                playsound('apoio.wav')

            elif 'horas' in command:
                time = datetime.now().strftime('%I:%M %p')
                spk('o horário correto é  ' + time)
                print("o horário correto é "+ time)
            elif ("piada" in command) or ("anedota" in command):
                piadoca()
            elif ("tchau" in command) or ("até logo" in command) or ("até mais" in command) or ("adeus" in command):
                think()
                f = open("datakkk.txt", "w")
                f.write("usada ultima vez em {}".format(data_em_dia_mes))
                f.close()
                spk("tchau")
                print("tchau")
                Notification(
                    title = "Corujinha disse",
                    description= "vou capotar agora, até outra hora, te amu",
                    duration=10).send()
                break
            elif "traduz" in command:
                tra = command.replace("traduz", "")
                think()
                translation = translator.translate(tra, dest='pt')

                print(translation.text)
                spk(translation.text)
            elif "quanto é " in command:
                legal = command.replace("quanto é" , "")
                think()
                translation = translator.translate(legal, dest='en')
                res = client.query(translation.text)
                output = next(res.results).text
                translatione = translator.translate(output, dest='pt')
                print(translatione.text)
                spk(translatione.text)
            elif "a melhor de todas" in command:
                think()
                playsound('the_best.wav')
            elif ("energia" in command) or ("bateria" in command) or ("carga" in command):
                think()
                arre = round(battery.percent)
                a = battery.power_plugged
                print("você tem {}%".format(arre))
                spk("você tem {} porcento".format(arre))
                if a == False and not arre <= 30:
                    print("lhe restam " + convertTime(battery.secsleft)+ " de uso")
                    spk("lhe restam "+ convertTime(battery.secsleft)+ " de uso")

                elif arre <= 30 and a == False:
                    print("a bateria está acabando, recomendo colocar o carregador no aparelho")
                    spk("a bateria está acabando, recomend o colocar o carregador no aparelho")
                    print("lhe restam " + convertTime(battery.secsleft)+ " de uso")
                    spk("lhe restam "+ convertTime(battery.secsleft)+ " de uso")
            elif "reiniciar" in command:
                try:
                    think()
                except:
                    print("sem conexões com o Arduino")
                os.system("python3 algoritmocorujinha.py")
                break
            elif ("diga" in command):
                kabum = command.replace("diga", "")
                think()
                print(kabum)
                spk(kabum)
            elif ("desligar" in command) or ("desligue" in command):
                think()
                try:
                    os.system("sudo shutdown -h -t 10")
                except:
                    os.system("shutdown -s -t 10")
            elif "verdade" in command:
                think()
                Serve()
            elif ("revelação" in command) or ("segredo" in command):
                think()
                revelations()
            elif "olhos" in command:
                olhos()
            elif "jogar" in command:
                jokenpo()
            elif "meu aniversário" in command:
                if data_em_dia_mes == "11/7":
                    print("é verdade, parabéns")
                    spk("é verdade, parabéns")
                else:
                    print("hmm, eu acho que não, seu aniversario é dia 11/7")
                    spk("hmm, eu acho que não, seu aniversario é dia 11/7")
            else:
                 think()
                 response = chatbot.get_response(command)
                 print(response)
                 spk(response)
    run_CORUJINHA()
CORUJINHA_MAIN()