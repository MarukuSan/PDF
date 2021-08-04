__authors__ = "RASANDISON Marc"
__contact__ = "0766182728"
__version__ = "1.0.0"
__date__ = "2021/07"

from PyPDF2 import PdfFileMerger

def recuperation(): 
	"""Récupère les fichiers à concaténer"""
	pass


def fusion():
	pdfs = []
	fin = False	# Indique la fin de la liste des fichiers
	i = 0	# Compte le nombre de fichiers à concatener

	while (fin!=True):
		nom_fichier = input("Nom du fichier ? ")
		if (nom_fichier==''):
			fin = True
		else:
			pdfs += [nom_fichier]
			i+=1

	if (pdfs==[]): 
	# Sort s'il n'y pas de fichier
		exit()

	merger = PdfFileMerger()

	for pdf in pdfs:
		merger.append(pdf)

	nom_final = input("Nom du fichier a generer ? ")	# Nom du fichier sortant
	merger.write(nom_final)
	merger.close()

fusion()