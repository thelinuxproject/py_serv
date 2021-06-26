#coding:utf-8
import socket
#import os
#import time

host, port = ("127.0.0.1",5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	socket.connect((host, port))
	print("Connexion Réussi !")

	#time.sleep(2)
	#os.system("clear")
	print("\n")
	data = input("Envoyer une commande au serveur\n--->")
	data = data.encode("utf8")
	socket.sendall(data)

except ConnectionRefusedError:
	print("Echec de la connexion\nServeur Introuvable ! ")
except:
	print("Connexion au seveur échouée !")
finally:
	socket.close()