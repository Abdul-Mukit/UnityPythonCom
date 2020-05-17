# from socket import socket, AF_INET, SOCK_DGRAM
#
# SERVER_IP = '192.168.0.3'
# port = 8080  # Make sure it's within the > 1024 $$ <65535 range
#
# s = socket()
# s.connect((SERVER_IP, port))
#
# message = input('-> ')
# while message != 'q':
#     s.send(message.encode('utf-8'))
#     data = s.recv(1024).decode('utf-8')
#     print('Received from server: ' + data)
#     message = input('==> ')
# s.close()



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
    message = input('-> ')
    mySocket.send(message.encode('utf-8'))
    time.sleep(.5)

sys.exit()



