# créer une fonction pour faire l'addition
def sum(a, b):
    return a + b


# créer une fonction pour faire la soustraction
def soustraction(a, b):
    return a - b


# créer une fonction pour faire la multiplication
def multiplication(a, b):
    return a * b


# créer une fonction qui permet d’éviter la division par zéro, et d’afficher un message
def division(a, b):
    if b != 0:
        return a / b
    else:
        print("Erreur : division par zéro")
