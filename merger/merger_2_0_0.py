__authors__ = "RASANDISON Marc"
__contact__ = "0766182728"
__version__ = "2.0.0"
__date__ = "2021/07"

import tkinter as tk
from PyPDF2 import PdfFileMerger

class Application(tk.Tk): 
    def __init__(self, title): 
        tk.Tk.__init__(self)
        self.title(title)
        self.geometry('300x150')
        self.pdfs = []
        self.create_entry()
        self.create_button('Add', self.add_and_delete)
        self.create_button('Submite', self.merger)       
        self.create_button_close()


    def delete_input(self): 
    	"""
			Description: Effacer le contenu d'une entrée
    	"""
    	self.entry.delete(0,tk.END)


    def add_and_delete(self):
   		self.add_pdf()
   		self.delete_input()


    def add_pdf(self): 
    	a = self.entry.get()
    	if (a != ''): 
    		self.pdfs += [a]
    		print(a+' a été ajouté')


    def create_button(self, text, command): 
    	"""
    		Fonction: Créer un bouton
    		Arguments: 'text' pour le texte à afficher sur le bouton
    			et 'command' pour la commande à faire pour un clic
    		Sortie: Un bouton
    	"""
    	self.bouton = tk.Button(self, text=text, command=command)
    	self.bouton.pack()


    def create_entry(self): 
    	"""
    		Fonction: Créer une entrée
    		Arguments: self
    		Sortie: Une zone de texte
    	"""
    	self.entry = tk.Entry(self)
    	self.entry.pack()


    def create_button_close(self): 
    	"""
    		Fonction: Créer un bouton pour fermer la fenêtre
    		Arguments: self
    		Sortie: Un bouton pour fermer la fenêtre
    	"""
    	self.button_close = tk.Button(self, text='Fermer', command=self.quit)
    	self.button_close.pack()


    def print_entry(self): 
    	"""
    		Fonction: Afficher dans la fenêtre ce que contient la 
    			zone de texte
    		Arguments: self
    		Sortie: Label avec le contenu de l'entrée
    	"""
    	tk.Label(self, text=self.entry.get()).pack()


    def print_label(self, text): 
    	"""
    		Fonction: Afficher un texte dans la fenêtre
    		Arguments: self et 'text' qui contient le texte à 
    			afficher
    		Sortie: Label avec le texte à afficher
    	"""
    	tk.Label(self, text=text).pack()


    def merger(self): 
    	if (self.pdfs==[]): 
    	# Sortir si pdfs est vide
    		exit()
    	else: 
    		result = PdfFileMerger()
    		
    		for pdf in self.pdfs:
    			result.append(pdf)

    		result.write('fusion.pdf')
    		result.close()



if __name__ == "__main__":
    app = Application("Maruku's app :)")
    app.mainloop()

