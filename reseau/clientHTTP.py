from socket import *

#serverName = raw_input('Nom du serveur?')
serverName = 'www.utt.fr'
serverPort = 80

page = '/fr/index.html'
# socket TCP
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# message = raw_input('data?')
requete = 'GET '+page+' HTTP/1.1\nHost: '+serverName+'\n\n\n'

print message

# envoi de la requete
clientSocket.send(message)

# recuperation et affichage de la reponse
modifiedMessage = clientSocket.recv(8192)
print modifiedMessage

# fermeture
clientSocket.close()


