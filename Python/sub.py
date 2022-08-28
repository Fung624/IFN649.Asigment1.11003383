import paho.mqtt.client as mqtt
import serial
import time
import string
def on_connect(client, userdata, flags, rc): # func for making connection
    print("Connected to MQTT")
    print("Connection returned result: " + str(rc) )
    client.subscribe("Data/#")
def on_message(client, userdata, msg): # Func for Sending msg
    ser = serial.Serial("/dev/rfcomm1", 9600)
    Array = str(msg.payload).split(" ")
    print(msg.topic)
    if(msg.topic=="Data/Soil"):
        if(int(Array[2][0])>0):
            ser.write(str.encode('BUZZER_ON'))
        else:
            ser.write(str.encode('BUZZER_OFF'))

    elif(msg.topic=="Data/Humidity"):
        if(int(Array[2][0:2])>70):
            ser.write(str.encode('LED_ON'))
        else:
            ser.write(str.encode('LED_OFF'))
        
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("3.26.175.255", 1883, 60)
client.loop_forever()
