from socket import *

serverName = "127.0.0.1"
serverPort = 12000

clientSocket = socket()
message = raw_input('data?')
print message
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()


