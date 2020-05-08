# from socket import socket, AF_INET, SOCK_DGRAM, gethostname
#
#
# host = gethostname()  # get local machine name
# port = 8080  # Make sure it's within the > 1024 $$ <65535 range
#
# s = socket()
# s.bind((host, port))
#
# print("Test server listening on port {0}\n".format(port))
# s.listen(1)
# client_socket, adress = s.accept()
# print("Connection from: " + str(adress))
# while True:
#     data = s.recv(1024).decode('utf-8')
#     if not data:
#         break
#     print('From online user: ' + data)
#     data = data.upper()
#     s.send(data.encode('utf-8'))
# s.close()


from socket import socket, gethostbyname, AF_INET, SOCK_DGRAM
import sys

PORT_NUMBER = 5000
SIZE = 1024

hostName = gethostbyname('0.0.0.0')

mySocket = socket(AF_INET, SOCK_DGRAM)
mySocket.bind((hostName, PORT_NUMBER))

print("Test server listening on port {0}\n".format(PORT_NUMBER))

while True:
    (data, addr) = mySocket.recvfrom(SIZE)
    print(data.decode('utf-8'))
