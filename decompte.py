#coding:utf-8

import time
import os

def decompte5sec(text):
	"""décompte et chargement fictif avec un text"""
	os.system("clear")
	charg = ""
	nb = 10

	while (charg != "••••••••••"):
		print(text+"\n")
		nb -= 1
		vide = nb * " "
		charg = charg + "•"
		chargement = "[" + charg + vide + "]"
		
		print(chargement)
		time.sleep(0.5)
		os.system("clear")