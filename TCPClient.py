from socket import *

serverName = "localhost"
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

command = input("Enter a command string (example. 'Random; 1; 10', 'Add; 1; 2', 'Subtract; 7; 4'): ")

clientSocket.send(command.encode())

modifiedSentence = clientSocket.recv(1024).decode()
print("From server:", modifiedSentence)

clientSocket.close()
