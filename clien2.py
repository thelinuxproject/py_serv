#coding:utf-8																		# [1]Encodage en UTF-8

import socket 																		# [3]Importation du module socket pour la connection
import os 																			# [4]Importation du module os pour la gestion du terminal
import time																			# [5]Importation du module time pour la gestion des temps 
from decompte import*

loop, invalid_connexion = (True,True)														# [8]Assignation des variable sous forme de Tuple

os.system("clear")

while invalid_connexion == True:															# [12]Boucle se saisie des information de connection

	host = input("[+] Saisir l'adresse(IP) du serveur :\n#--> ")									# [14]Demander l'adresse du serveur
	port = input("[+] Saisir le port de communication\n#--> ")										# [15]Demander le port de communication
	
	if host =="exit()" or port =="exit()":															# [17]Quitter le programme
		loop = False
		invalid_connexion = False

	try:
		port = int(port)
		if port < 0:																# [23]Teste de la Validiter du port saisie par l'utilisateur			
			decompte5sec("[+] Le Nombre saisie est inferieur à 0\n[+] veuillez saisir un nombre (de 0 à 65535)")	# [24]Message signalisant la non conformiter de la saisie [saisie <à 0]
			
		elif port > 65535:
			decompte5sec("[+] Le Nombre saisie est superieur à 65535\n[+] veuillez saisir un nombre (de 0 à 65535)")
			
		else:
			decompte5sec("[+] Connexion en cour :")											# [30]Attente facultative
			try:
				socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				socket.connect((host, port))
				invalid_connexion = False
				print("[+] Connexion Réussi !")											# [35]Message afficher si auccune erreur ne survient lors de la connexion au serveur 
			except ConnectionRefusedError:
				print("[+] Echèc de la connection\n[+] Serveur Introuvable")						# [37]Message généré quand le serveur est introuvable
			except:
				print("[+] Echèc de la connection")


	except:
		print("[+] veuillez saisir un NOMBRE de 0 à 65535)")										# [43]Gestion des Erreur lors du Caste de la saisie du port

while loop == True:																	# [45]Création de la boucle pour rester connecter jusqua la sortie
	data = input("\n#--> ")
	if data != "exit()":
		data = data.encode("utf8")														# [48]Encodage de la variable en utf8
		socket.sendall(data)															# [49]Communication de la commande encoder (data)
	else:
		loop = 0																	# [51]Sortie de la boucle pour se déconnecter du serveur
socket.close()																		# [52]Fermeture socket