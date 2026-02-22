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

        elif char in "+-*/x":
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

        # Note: view now provides separate '(' and ')' buttons so special-case
        # handling for '()' is no longer required.

        elif char==")":
            if self.actuel:
                self.expression.append(self.actuel)
            self.expression.append(")")
            self.actuel=""
            self.view.set_display(")")

        # Functions that expect an argument: append function name and an
        # opening parenthesis so the model receives tokens like ['sin','(','0',')'].
        # We'll auto-close any unmatched parentheses before evaluation.
        elif char in ("sin", "cos", "tan", "√", "log", "ln", "eˣ"):
            if self.actuel:
                self.expression.append(self.actuel)
            # append function token and an explicit '('
            self.expression.append(char)
            self.expression.append("(")
            self.actuel = ""
            # display a user-friendly function prompt
            display_text = f"{char}(" if char != "eˣ" else "e^("
            self.view.set_display(display_text)
 
 
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

        # Before evaluation, auto-close any unmatched '(' tokens so expressions
        # like ['sin','(','0'] become ['sin','(','0',')'] for the model.
        elif char == "=":
            if self.actuel:
                self.expression.append(self.actuel)

            # auto-close parentheses
            open_count = self.expression.count('(')
            close_count = self.expression.count(')')
            while close_count < open_count:
                self.expression.append(')')
                close_count += 1

            try:
                result=self.model.calculate(self.expression)
                self.view.set_display(result)
                self.expression=[]
                self.actuel=result
            except:
                self.view.set_display("Error")
                self.expression=[]
                self.actuel=""

     