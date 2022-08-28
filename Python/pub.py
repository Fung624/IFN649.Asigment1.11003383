import serial
import time
import string
import paho.mqtt.publish as publish
# reading and writing data from and to arduino serially.
# rfcomm0 -> this could be different
ser = serial.Serial("/dev/rfcomm0", 9600)
ser.write(str.encode('Start\r\n'))
ser1 = serial.Serial("/dev/rfcomm2", 9600)
ser1.write(str.encode('Start\r\n'))
while True:
    if ser.in_waiting > 0:
        rawserial = ser.readline()
        cookedserial = rawserial.decode('utf-8').strip('\r\n')
        print(cookedserial)
        publish.single("Data/Humidity", cookedserial, hostname="3.26.175.255")
    if ser1.in_waiting > 0:
        rawserial1 = ser1.readline()
        cookedserial1 = rawserial1.decode('utf-8').strip('\r\n')
        print(cookedserial1)
        publish.single("Data/Soil", cookedserial1, hostname="3.26.175.255")
print("Done")