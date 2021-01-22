from __future__ import print_function
from socket import *

bind = '127.0.0.1'
port = 1234

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((bind, port))

while True:
    message, address = serverSocket.recvfrom(2048)
    print(".", end='', flush=True)
    serverSocket.sendto(message, address)