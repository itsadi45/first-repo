from socket import *
import threading
import os
serverPort = 5050

def startServer():
    os.system("wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
    os.system("unzip -qq -n ngrok-stable-linux-amd64.zip")
    os.system("ngrok authtoken ")
    os.system("")
    
    
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))

while True:
    (message, clientAddress) = serverSocket.recvfrom(2048)
    modified = message.upper()
    serverSocket.sendto(modified, clientAddress)
