import paho.mqtt.client as mqtt

#primeiro connect
def ao_conectar(client, userdata, flags, rc):
    print("Nos conectamos com o seguinte código de resultado {}".format(str(rc)))

#metodo chamado quando receber msg
def ao_receber(client, userdate, msg):
    print("{} --- {}".format(msg.topic, str(msg.payload)))


client = mqtt.Client()

client.on_connect = ao_conectar
client.on_message = ao_receber
client.connect("broker.hivemq.com",1883,60)
client.subscribe("aula/andre/4ecr")
client.loop_forever()
while True:
    client.publish("aula/andre/4ecr", input("envie mensagem"))#publica algo em topico
cliente.loop_finish()