#CNC server
from socket import *

serverPort = 8000

# Create IPv4, TCP socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)

print("CNC listening...")
connectionSocket, addr = serverSocket.accept()
print("wazzup " + str(addr))
message = connectionSocket.recv(1024)
print(message)
command = ""

while command != "exit":
	command = input("Enter a command: ")
	connectionSocket.send(command.encode())
	message = connectionSocket.recv(1024).decode()
	print(message)

connectionSocket.shutdown(SHUT_RDWR)
connectionSocket.close()