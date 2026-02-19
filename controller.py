class CalculatorController: #creation de la class calculatorcontroller

    def __init__(self, model, view): #constructeur de la class

        self.model = model
        self.view = view

        self.actuel = "" #variable string pour stocker les donnees saisi par l'utilisateur en temps reel
        self.expression = [] #liste pour conserver les donnes rentrer par l'utilisateur

        for key, btn in self.view.buttons.items(): #recuperation de la cle et les valeur des bouton 
            btn.configure(command=lambda x=key:self.on_click(x)) #configuration d'une action pour chaque boutons

    def on_click(self, char): #methode pour determiner l'action des boutons qui prend char comme parametre

        if char.isdigit() or char==".":
            self.actuel += char
            self.view.set_display(self.actuel)

        elif char in "+-*/":
            if self.actuel:
                self.expression.append(self.actuel)
                self.expression.append(char)
                self.actuel=""
                self.view.set_display(char)

        elif char=="=":
            if self.actuel:
                self.expression.append(self.actuel)

            try:
                result=self.model.calculate(self.expression)
                self.view.set_display(result)
                self.expression=[]
                self.actuel=result
            except:
                self.view.set_display("Error")
                self.expression=[]
                self.actuel=""

        elif char=="C":
            self.actuel=""
            self.expression=[]
            self.view.set_display("")

        elif char=="⌫":
            self.actuel=self.actuel[:-1]
            self.view.set_display(self.actuel)

        elif char=="(":
            if self.actuel:
                self.expression.append(self.actuel)
            self.expression.append("(")
            self.actuel=""
            self.view.set_display("(")

        elif char==")":
            if self.actuel:
                self.expression.append(self.actuel)
            self.expression.append(")")
            self.actuel=""
            self.view.set_display(")")

        elif char=="sin":
            if self.actuel:
                self.expression.append(self.actuel)
            self.expression.append("sin")
            self.actuel=""
            self.view.set_display("sin(")

        elif char=="cos":
            if self.actuel:
                self.expression.append(self.actuel)
            self.expression.append("cos")
            self.actuel=""
            self.view.set_display("cos(")

        elif char=="tan":
            if self.actuel:
                self.expression.append(self.actuel)
            self.expression.append("tan")
            self.actuel=""
            self.view.set_display("tan(")
 
 
        elif char=="%":
            if self.actuel:
                self.expression.append(self.actuel)
            self.expression.append("%")
            self.actuel=""
            self.view.set_display("%")

        elif char == "ⁿ√":
            if self.actuel:
                self.expression.append(self.actuel)
            self.expression.append("ⁿ√")
            self.actuel=""
            self.view.set_display("ⁿ√(")

     