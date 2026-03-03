#view.py
#ici on cree l'affichage graphique de la calculatrice.

import customtkinter as ctk #importation de la bibliothèque customtkinter et attribution de l'alias "ctk" pour faciliter son utilisation dans le code
import tkinter as tk
ctk.set_appearance_mode('light')
ctk.set_default_color_theme('blue')
class CalculatorView(ctk.CTk): #création de la classe CalculatorView qui hérite de la classe CTk de la bibliothèque customtkinter

    def __init__(self): #constructeur de la classe CalculatorView
        super().__init__() #appel du constructeur de la classe parente (CTk)
        #configuration de la fenetre principal
        self.title("Calculatrice") #titre de la fenêtre
        #taille de la fenêtre
        self.geometry("350x450") 
        self.minsize(350, 450)
        self.maxsize(350, 450)
        self.iconbitmap('logo-calculatrice.ico')
        self.configure(fg_color=("#FFFFFF","#121212"))
        self.attributes('-topmost', True)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        self.bind("<Escape>", lambda event: self.quit())

        ################################################################################################################
        #configuration des principaux widgets de l'app
        
        #history_frame et widgets
        self.history_fenetre = ctk.CTkFrame(self, fg_color=("#FFFFFF","#121212"))
        self.history_fenetre.grid_columnconfigure(0, weight = 1, uniform = 'a')
        self.history_fenetre.grid_columnconfigure(1, weight = 1, uniform = 'a')
        self.history_fenetre.grid_rowconfigure((0,1,2,3,4,5,6,7,8,9), weight=1)
        self.history_fenetre.grid_remove()
        
        self.textebox = ctk.CTkTextbox(self.history_fenetre, font=("Segoe UI",18), height=80, corner_radius=5, fg_color=("#FFFFFF","#121212"),text_color=("black","white"), border_width=0)
        self.button_panier = ctk.CTkButton(self.history_fenetre, text ="🗑",font=("Segoe UI", 15), text_color = ("#528DD0","#3F3A3A"), fg_color=("#FFFFFF","#121212"), border_width=0, hover_color=("#71C9FF","#696060") )
        self.button_delete = ctk.CTkButton(self.history_fenetre, text ="EFF",font=("Segoe UI", 15), text_color = ("#528DD0","#3F3A3A"), fg_color=("#FFFFFF","#121212"), border_width=0, hover_color=("#71C9FF","#696060") )
        
        #self.calcule frame et widgets
        self.calcul_fenetre = ctk.CTkFrame(self, fg_color=("#FFFFFF","#121212"), width = 400) 
        self.calcul_fenetre.grid( row = 0, column= 0, columnspan = 2,  sticky = "wens")
        

        self.display = ctk.CTkEntry(self.calcul_fenetre, font=("Segoe UI",26, 'bold'), justify="right", height=80, corner_radius=20, fg_color=("#FFFFFF","#121212"),text_color=("black","white"), border_width=0) #creation d'un espace d'affichage pour les calculs
        self.display.grid(row=1,column=0,columnspan=4, rowspan = 2, sticky="nsew",padx=5,pady=5)#positionnement sur la grille et moyen d'affichage de l'espace de calcul

        theme_switch = ctk.CTkSwitch(self.calcul_fenetre, font=("Segoe UI",12),  text = ("Sombre"),text_color=("black","white"), command = self.apparence, fg_color = ("#7EB5F4","#222222"), progress_color=("#7EB5F4","#222222"), button_color=("#528DD0","#3F3A3A"),button_hover_color=("#71C9FF","#696060"))
        theme_switch.grid(row = 0, column = 0, padx = 5, pady = 5, columnspan = 2)

        button1 = ctk.CTkButton(self.calcul_fenetre, text ="⏱",font=("Segoe UI", 20), text_color = ("#528DD0","#3F3A3A"), fg_color=("#FFFFFF","#121212"), border_width=0, hover_color=("#71C9FF","#696060" ))
        button1.grid(row = 0, column = 3, padx = 5, pady = 5)

        self.buttons = {} #creation d'une bibliotheque pour stocker l'index et la valeur "string" de chaque bouton
        # Added 'log' to the small UI so users can compute log(x) directly.
        btns = [
            'π','%','√','⌫',
            '(',')','MOD','C',
            '7','8','9','+',
            '4','5','6','-',
            '1', '2', '3', 'x',
            '±','0','.','/', 
                 '=',

        ] #liste des boutons de la calculatrice basique

        for i, b in enumerate(btns): #parcours de la liste des boutons avec un index "i" pour le positionnement et une valeur "b" pour le texte du bouton
            # Couleurs par catégorie


            if b in ['π', '√', '±', '%', 'MOD', '(', ')', '.','C', '⌫','+', '-', 'x', '/','=']:
                fg = ("#52AFDE","#2E2C2C" )     # fonctions blue pale
                hover = ("#04A9FB","#262222")
                

            else:
                fg = ("#528DD0","#3F3A3A")    # gris sombre chiffres
                hover = ("#71C9FF","#696060")
                

            btn = ctk.CTkButton(
                self.calcul_fenetre,
                text=b,
                font=("Segoe UI", 20),
                corner_radius=10,
                fg_color=fg,
                hover_color=hover,
                text_color = ("#FFFFFF", "#3EB3EE")
            )

            btn.grid(row=(i//4)+3,column=i%4,sticky="nsew",padx=2,pady=2) #positionnement du bouton sur la grille en fonction de son index "i" et moyen d'affichage du bouton
            self.buttons[b] = btn #stockage du bouton dans la bibliotheque "buttons" avec comme index le texte du bouton "b" et comme valeur le bouton lui même "btn"
        self.buttons['⏱'] = button1
        self.buttons["🗑"] = self.button_panier
        self.buttons["EFF"] = self.button_delete

        for i in range(10): #configuration de la grille pour que les lignes et les colonnes s'adaptent à la taille de la fenêtre
            self.calcul_fenetre.grid_rowconfigure(i,weight=1, uniform = 'a') #configuration de la ligne "i" pour qu'elle s'adapte à la taille de la fenêtre
        for i in range(4): #configuration de la colonne "i" pour qu'elle s'adapte à la taille de la fenêtre
            self.calcul_fenetre.grid_columnconfigure(i,weight=1, uniform = 'a') #configuration de la colonne "i" pour qu'elle s'adapte à la taille de la fenêtre

        self.buttons["="].grid_configure(columnspan=4, rowspan = 2)
        
    def set_display(self, text): #fonction pour mettre à jour l'affichage de la calculatrice avec le texte "text"
        # Use tkinter constant END (ctk does not expose END)
        self.display.delete(0, tk.END) #efface le contenu actuel du champ d'affichage
        self.display.insert(0, text) #insère le texte dans le champ d'affichage

    def apparence(self):
        current_mode = ctk.get_appearance_mode()  # récupère le mode actuel
        if current_mode == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")

    def history_fenetre_fonc (self, historie):
        self.geometry("550x450")
        self.minsize(550, 450)
        self.maxsize(650,450)
        self.grid_columnconfigure((0,1), weight = 3)
        self.grid_columnconfigure(2, weight = 1)
        self.grid_rowconfigure(0, weight=1)
        self.calcul_fenetre.grid( row = 0, column= 0, columnspan = 2,  sticky = "wens")
        self.history_fenetre.grid(padx=5, pady=5, sticky = "nsew", row = 0, column = 2)
        self.textebox.grid(sticky="nsew", row = 0, column = 0, columnspan = 2, rowspan = 9)
        self.button_panier.grid(row = 9, column = 0, sticky = "we" )
        self.button_delete.grid(row=9, column=1, sticky="we")
        self.textebox.configure(state = "normal")
        self.textebox.delete('1.0', "end")
        self.textebox.insert('end', historie)
        self.textebox.configure(state = "disabled")

    def wind_norm(self):
        self.geometry("350x450")
        self.maxsize(350, 450)
        self.minsize(350, 450)
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0,1), weight=1)
        self.bind("<Escape>", lambda event: self.quit())


