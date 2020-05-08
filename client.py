import sys
from socket import socket, AF_INET, SOCK_DGRAM
import time

SERVER_IP = '192.168.0.3'
PORT_NUMBER = 5000
SIZE = 1024
print("Test client sending packets to IP {0}, via port {1}\n".format(SERVER_IP, PORT_NUMBER))

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.connect((SERVER_IP,PORT_NUMBER))

while True:
    mySocket.send('cool')
    time.sleep(.5)

sys.exit()



