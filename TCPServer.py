import threading
from socket import *

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

    if len(splitSentence) != 3:
        result = "Invalid input format"
    else:
        command, num1, num2 = splitSentence
        num1 = int(num1)
        num2 = int(num2)

        if command == "Random":
            import random
            result = str(random.randint(num1, num2))
        elif command == "Add":
            result = str(num1 + num2)
        elif command == "Subtract":
            result = str(num1 - num2)
        else:
            result = "Invalid command"

    connectionSocket.send(result.encode())
    connectionSocket.close()

while True:
    connectionSocket, addr = serverSocket.accept()
    print("Client connected")
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()
