from socket import *
serverPort = 5050

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))

while True:
    (message, clientAddress) = serverSocket.recvfrom(2048)
    modified = message.upper()
    serverSocket.sendto(modified, clientAddress)
