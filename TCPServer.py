import threading
from socket import *
import random

serverName = "localHost"
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind((serverName, serverPort))
serverSocket.listen(1)
print("The server is ready to receive")

def handleClient(connectionSocket, address):
    sentence = connectionSocket.recv(1024).decode()
    print(f"Received: {sentence}")
    splitSentence = sentence.split(';')

    if len(splitSentence) != 3 or splitSentence[0] not in ["Random", "Add", "Subtract"]:
        result = "Invalid input format"
    else:
        num1 = int(splitSentence[1])
        num2 = int(splitSentence[2])
        if splitSentence[0] == "Random":
            result = str(random.randint(num1, num2))
        elif splitSentence[0] == "Add":
            result = str(num1 + num2)
        elif splitSentence[0] == "Subtract":
            result = str(num1 - num2)

    connectionSocket.send(result.encode())
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Client connected")
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
