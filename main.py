from socket import *
import threading
import urllib
import os
serverPort = 5050

def startNGROKServer():
    time.sleep(1)
    os.system("wget -q -c -nc https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip")
    os.system("unzip -qq -n ngrok-stable-linux-amd64.zip")
    os.system("ngrok authtoken 2AZ6Q4rkOlX4Lk8Wyl2p6LeSzm5_86zUyKaEBTBdMDf9nrQjV")
    os.system("ngrok tcp 5050")
    
    with urllib.request.urlopen('http://localhost:4040/api/tunnels') as response:
        data = json.loads(response.read().decode())
        (host, port) = data['tunnels'][0]['public_url'][6:].split(':')
        return (host,port)
    
def startLocalServer():
    os.system("python3 -m http.server 5050")
    
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('localhost', serverPort))

while True:
    (message, clientAddress) = serverSocket.recvfrom(2048)
    modified = message.upper()
    serverSocket.sendto(modified, clientAddress)
