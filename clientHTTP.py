from socket import *

#serverName = raw_input('Nom du serveur?')
serverName = 'www.utt.fr'
serverPort = 80

page = '/fr/index.html'
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
# message = raw_input('data?')
message='GET '+page+' HTTP/1.1\nHost: '+serverName+'\n\n\n'

print message

clientSocket.send(message)

modifiedMessage = clientSocket.recv(8192)
print modifiedMessage
clientSocket.close()


