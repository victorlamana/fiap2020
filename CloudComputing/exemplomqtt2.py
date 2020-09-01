import paho.mqtt.client as mqtt
import webbrowser
import os
from playsound import playsound

#primeiro connect
def ao_conectar(client, userdata, flags, rc):
    print("Nos conectamos com o seguinte código de resultado {}".format(str(rc)))


#metodo chamado quando receber msg
def ao_receber(client, userdate, msg):
    print("{} --- {}".format(msg.topic, str(msg.payload)))
    if 'DESLIGAR' in str(msg.payload).upper():
        os.system("shutdown -s")
        print ("desligou")
    elif "FIAP" in str(msg.payload).upper():
        webbrowser.open("www.fiap.com.br")
    elif "USUARIO" in str(msg.payload).upper():
        client.publish("aula/andre/otavio", os.getlogin())
    elif "ALARME" in str(msg.payload).upper():
        playsound("C:\\Users\\VICTOR\\Documents\\sonzera\\alarme.mp3")

client = mqtt.Client()

client.on_connect = ao_conectar
client.on_message = ao_receber
client.connect("broker.hivemq.com",1883,60)
client.subscribe("aula/andre/otavio")
client.loop_forever()
