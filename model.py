import math as m # importation de la bibliotheque mathematique comme "m" pour faciliter son usage

class CalculatorModel: #creation de la classe du model de la calculatrice pour mettre la logique de calcul et les fonctions de calcul

    def calculate(self, liste_expression): #fonction pour calculer le resultat des calculs de l'utilisateur en prenant une liste d'expression "expression_list" comme argument qui stocke les nombres et les opérateurs de l'expression à calculer
        # Build a safe expression string from a token list and evaluate using
        # the math module. The previous implementation attempted to cast
        # operator strings to float and had incorrect branching which caused
        # crashes. This implementation maps known tokens to Python/math
        # equivalents and falls back to a simple eval for arithmetic.
        if not liste_expression:
            return ""

        # Map some tokens to Python equivalents
        mapped = []
        for tok in liste_expression:
            if tok == 'x':
                mapped.append('*')
            elif tok == 'π':
                mapped.append(str(m.pi))
            elif tok == 'e':
                mapped.append(str(m.e))
            elif tok == 'mod':
                mapped.append('%')
            else:
                mapped.append(tok)

        expr = ''.join(mapped)

        # Replace function names with math module equivalents so eval can use them
        expr = expr.replace('sin', 'm.sin')
        expr = expr.replace('cos', 'm.cos')
        expr = expr.replace('tan', 'm.tan')
        expr = expr.replace('ln', 'm.log')
        expr = expr.replace('log', 'm.log10')
        expr = expr.replace('√', 'm.sqrt')
        expr = expr.replace('eˣ', 'm.exp')

        try:
            # Evaluate with a restricted global namespace exposing only math
            result = eval(expr, {"__builtins__": None, 'm': m})
        except Exception:
            # If evaluation fails, return an error string like the UI expects
            return "Error"

        return str(result)
    
  
