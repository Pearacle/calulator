#Exo 1 : Devine le nombre
import random

def devinette():
    secret = random.randint(0, 100)  # générer un nombre de 0 à 100
    
    n = None
    while n != secret: # faire ceci Tant que le nombre(n) entré par l'utilisateur sera différent de le nombre (secret) 
        n = int(input("Entrez votre nombre: "))
        #si le nombre entré est inférieur au nombre secret
        if n < secret:
            print("Trop petit! Essayez encore.")
        # si le nombre entré est supérieure au nombre secret
        elif n > secret:
            print("Trop grand! Essayez encore.")
    
    print("Exact!")
# Appel de la fonction
devinette()




    
