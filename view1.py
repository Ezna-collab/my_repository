#view.py
#ici on cree l'affichage graphique de la calculatrice.

from tkinter import Tk
import customtkinter as ctk #importation de la bibliothèque customtkinter et attribution de l'alias "ctk" pour faciliter son utilisation dans le code

class CalculatorView(ctk.CTk): #création de la classe CalculatorView qui hérite de la classe CTk de la bibliothèque customtkinter
    super().__init__() #appel du constructeur de la classe parente (CTk)


    calculatrice_simple = Tk.frame
    calculatrice_scientifique = Tk.frame

    def Erreur(self): #fonction pour afficher "Error" en cas d'erreur de calcul dans la calculatrice scientifique
        self.display.delete(0,ctk.END) #efface le contenu actuel du champ d'affichage de l'interface utilisateur commencant à l'index 0 jusqu'à la fin du texte pour la calculatrice scientifique
        self.display.insert(0,"Error") #insère le texte "Error" dans le champ d'affichage de l'interface utilisateur à l'index 0, ce qui signifie que le texte "Error" sera affiché au début du champ d'affichage pour la calculatrice scientifique

    def set_display(self, text): #fonction pour mettre à jour l'affichage de la calculatrice avec le texte "text"
        self.display.delete(0,ctk.END) #efface le contenu actuel du champ d'affichage de l'interface utilisateur commencant à l'index 0 jusqu'à la fin du texte
        self.display.insert(0,text) #insère le texte "text" dans le champ d'affichage de l'interface utilisateur à l'index 0, ce qui signifie que le texte sera affiché au début du champ d'affichage.

class Simple_calculatrice(CalculatorView): #création de la classe Simple_calculatrice qui hérite de la classe CalculatorView pour une calculatrice basique
    def __init__(self):
        super().__init__()

        self.title("Calculatrice basique") #titre de la fenêtre
        self.geometry("300x600") #taille de la fenêtre

        self.display = ctk.CTkEntry(self, font=("Arial",24), justify="right") #creation d'un espace d'affichage pour les calculs
        self.display.grid(row=0,column=0,columnspan=4,sticky="nsew",padx=10,pady=10) #positionnement sur la grille et moyen d'affichage de l'espace de calcul

        self.buttons = {} #creation d'une bibliotheque pour stocker l'index et la valeur "string" de chaque bouton
        btns = [
                        '⌫',
            'C','()','%','Ω',
            '7','8','9','+',
            '4','5','6','-',
            '1','2','3','x',
            '±','0','.','/',
                '=',

        ] #liste des boutons de la calculatrice basique

        for i, b in enumerate(btns): #parcours de la liste des boutons avec un index "i" pour le positionnement et une valeur "b" pour le texte du bouton
            btn = ctk.CTkButton(self,text=b) #creation d'un bouton avec le texte "b" et la classe CTkButton
            btn.grid(row=(i//4)+1,column=i%4,sticky="nsew",padx=5,pady=5) #positionnement du bouton sur la grille en fonction de son index "i" et moyen d'affichage du bouton
            self.buttons[b] = btn #stockage du bouton dans la bibliotheque "buttons" avec comme index le texte du bouton "b" et comme valeur le bouton lui même "btn"

        for i in range(7): #configuration de la grille pour que les lignes et les colonnes s'adaptent à la taille de la fenêtre
            self.grid_rowconfigure(i,weight=1) #configuration de la ligne "i" pour qu'elle s'adapte à la taille de la fenêtre
        for i in range(5): #configuration de la colonne "i" pour qu'elle s'adapte à la taille de la fenêtre
            self.grid_columnconfigure(i,weight=1) #configuration de la colonne "i" pour qu'elle s'adapte à la taille de la fenêtre

        super().set_display("") #appel de la fonction set_display de la classe parente pour initialiser l'affichage de la calculatrice basique à une chaîne vide
        super().Erreur() #appel de la fonction Erreur de la classe parente pour initialiser l'affichage de la calculatrice basique à "Error" en cas d'erreur de calcul

           

class calculator_large(CalculatorView): #création de la classe calculator_large qui hérite de la classe CTk de la bibliothèque customtkinter pour une calculatrice scientifique plus grande

    def __init__(self): #constructeur de la classe calculator_large
        super().__init__() #appel du constructeur de la classe parente 

        self.title("Calculatrice scientifique") #titre de la fenêtre
        self.geometry("750x600") #taille de la fenêtre de la calculatrice scientifique

        self.display = ctk.CTkEntry(self, font=("Arial",24), justify="right") #creation d'un espace d'affichage pour les calculs de la grande calculatrice
        self.display.grid(row=0,column=0,columnspan=7,sticky="nsew",padx=10,pady=10) #positionnement sur la grille et moyen d'affichage de l'espace de calcul de la grande calculatrice

        self.buttons = {} #creation d'une bibliotheque pour stocker l'index et la valeur "string" de chaque bouton de la grande calculatrice
        btns = [
                        '⌫',
            'π','DEG','√',      'C','()','%','+',
            'sin','cos','tan',  '7','8','9','-',
            'ln','log','1/x',   '4','5','6','*',
            'eˣ','xⁿ','mod',    '1','2','3','/',
                 'Ω',           '±','0','.','=',
                  

        ] #liste des boutons plus nombreux de la calculatrice scientifique

        for i, b in enumerate(btns): #parcours de la liste des boutons avec un index "i" pour le positionnement et une valeur "b" pour le texte du bouton
            btn = ctk.CTkButton(self,text=b,font=("Arial",24)) #creation d'un bouton avec le texte "b", la classe CTkButton et une taille de police plus grande pour la calculatrice scientifique
            btn.grid(row=(i//7)+1,column=i%7,sticky="nsew",padx=5,pady=5) #positionnement du bouton sur la grille en fonction de son index "i" et moyen d'affichage du bouton pour la calculatrice scientifique
            self.buttons[b] = btn #stockage du bouton dans la bibliotheque "buttons" avec comme index le texte du bouton "b" et comme valeur le bouton lui même "btn" pour la calculatrice scientifique

        for i in range(7): #configuration de la grille pour que les lignes et les colonnes s'adaptent à la taille de la fenêtre de la calculatrice scientifique
            self.grid_rowconfigure(i,weight=1) #configuration de la ligne "i" pour qu'elle s'adapte à la taille de la fenêtre de la calculatrice scientifique
        for i in range(7): #configuration de la colonne "i" pour qu'elle s'adapte à la taille de la fenêtre de la calculatrice scientifique
            self.grid_columnconfigure(i,weight=1) #configuration de la colonne "i" pour qu'elle s'adapte à la taille de la fenêtre de la calculatrice scientifique

        super().set_display("") #appel de la fonction set_display de la classe parente pour initialiser l'affichage de la calculatrice basique à une chaîne vide
        super().Erreur() #appel de la fonction Erreur de la classe parente pour initialiser l'affichage de la calculatrice basique à "Error" en cas d'erreur de calcul

    

