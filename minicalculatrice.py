"""Créer une mini calculatrice """

# Créer une fonction pour souhaiter la bienvenue 
def afficher_message_accueil():
    print("Bienvenue sur la mini-calculatrice !")

# creer une fonction qui permet de récupérer les nombres saisis par l'utilisateur
def saisir_deux_nombres():
    num1 = float(input("Entrez le premier nombre : "))
    num2 = float(input("Entrez le deuxième nombre : "))
    return num1, num2

# créer une fonction qui permet de demander à l'utilisateur quelle opération il souhaite effectuer :
def afficher_menu_et_faire_choix():
    print("=== MENU ===")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")

    choix_utilisateur = input("Entrez votre choix (1-4) : ")

    # créer une boucle qui permet de s’assurer de la saisie de l’utilisateur
    while choix_utilisateur not in ["1", "2", "3", "4"]:
        choix_utilisateur = input("Choix invalide. Entrez votre choix (1-4) : ")

    return choix_utilisateur

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

# créer une fonction qui permet de lancer l'opération en fonction du choix de l’utilisateur
def run_calculation(choix_utilisateur):
    num1, num2 = saisir_deux_nombres()
    match choix_utilisateur:
        case "1":
            result = sum(num1, num2)
        case "2":
            result = soustraction(num1, num2)
        case "3":
            result = multiplication(num1, num2)
        case "4":
            result = division(num1, num2)
        case _:
            print("Choix invalide.")
    return result


if __name__ == "__main__":
    
    afficher_message_accueil()
    choix_utilisateur = afficher_menu_et_faire_choix()
    result = run_calculation(choix_utilisateur)
    print(result)


# créer une fonction permet de calculer la moyenne des nombres stockés dans la liste nombres
def calculer_moyenne(nombres):
    total = 0
    for nombre in nombres:
        total += nombre
    moyenne = total / len(nombres)
    return moyenne
