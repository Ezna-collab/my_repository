import math as m # importation de la bibliotheque mathematique comme "m" pour faciliter son usage

class CalculatorModel: #creation de la classe du model de la calculatrice pour mettre la logique de calcul et les fonctions de calcul

    def calculate(self, liste_expression): #fonction pour calculer le resultat des calculs de l'utilisateur en prenant une liste d'expression "expression_list" comme argument qui stocke les nombres et les opérateurs de l'expression à calculer
        total = float(liste_expression[0]) #creation de la variable "total"  qui contient le premier element de la liste d'espression converti de string a float pour pouvoir effectuer des calcules avec les nombres entier et a virgule


        i = 1 #creation de la variable "i" qui contient l'index de l'operateur de l'operation a effectuer


        while i < len(liste_expression): #creation d'une boucle while qui continue du moment que la variable "i" est inferieur a la longueur de la liste d'espression 
            operator = liste_expression[i] #variable de l'operation qui prend pour valeur initial le deuxieme elememt de la liste d'espression
            number = float(liste_expression[i+1]) #variable number qui prend la troisieme valeur de la liste d'expression

           
            #pour les operations ou l'operateur sera rentrer en deuxieme
            if operator in ["+","-","*","/","%","1/x","xⁿ","ⁿ√","mod"]:

                if operator == "+": #si l'operation est le signe de l'addition on effectue une addition
                    total += number #additionnement du premier nombre de la liste d'espression avec le troisieme
                
                elif operator == "-":#si l'operation est le signe de la soustraction on effectue une soustraction
                    total -= number #soustraction du premier nombre de la liste d'espression avec le troisieme
                
                elif operator == "*" or operator == "x":#si l'operation est le signe de la multiplication on effectue une multiplication
                    total *= number #multiplication du premier nombre de la liste d'espression avec le troisieme
                
                elif operator == "/":#si l'operation est le signe de la division on effectue une division
                    total /= number #division du premier nombre de la liste d'espression avec le troisieme
                
                elif operator == "%":#si l'operation est le signe de pourcentage on effectue une pourcentage
                    total = total * number / 100
                
                elif operator == "1/x":
                    total = 1/total

                elif operator == "ⁿ√":
                    total = m.pow(total, 1/number)
                
                elif operator == "xⁿ":
                    total = m.pow(total,number)

                elif operator == "mod":
                    if total % 2 == 0:
                        total = "PAIRE"
                    else:
                        total = "IMPAIRE"
            

            

            ##pour les operations ou l'operateur sera rentrer en premier

            elif operator in ["√","ln","log","eˣ","sin","cos","tan","π","e","DEG"]:
                total, operator = float(operator), str(total)

                if operator == "√":
                    total = m.sqrt(total)

                elif operator == "ln":
                    total = m.log(total, 2.71828)

                elif operator == "log":
                    total = m.log(total)

                elif operator == "eˣ":
                    total = m.exp(total)

                elif operator == "sin":
                    total = m.sin(total)

                elif operator == "cos":
                    total = m.cos(total)

                elif operator == "tan":
                    total = m.tan(total)

                elif operator == "π":
                    total = m.pi

                elif operator == "e":
                    total = m.e

                elif operator == "DEG":
                    total = m.degrees(total)

            i += 2

        return str(total)
    
  
