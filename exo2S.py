"""
Exercice 1 : Devine le nombre (niveau avancé avec limite de valeurs)
Modifie ton programme de devinette pour que l'utilisateur puisse lui-même choisir la plage de valeurs dans laquelle le nombre mystère sera 
généré. Demande-lui de fournir une borne inférieur et une borne supérieure avant de commencer la partie. 
Comme précédemment, l'utilisateur a 3 tentatives pour deviner le nombre.
"""
import random

def devinette():
    borne_inferieur = int(input('Entrer la bonne inferieur :'))
    borne_superieur = int(input("Entrer la bonne supérieure :"))
    
    tentatives = 3
    
    plage = random.randint(borne_inferieur,borne_superieur)
    
    for essai in range(tentatives):
        nbre_secret = int(input(f"Tentatives{essai + 1}/{tentatives} :Devinez le nombre entre {borne_inferieur} et {borne_superieur} : "))    
        if nbre_secret < plage:
            print('Trop petit')
        elif nbre_secret > plage:
            print('Trop grand')
        else:
            print("Exact! Vous avez trouvé le nombre!")
        
    
    print(f"Vous avez épuisé vos {tentatives} tentatives. Le nombre secret était {plage}.")


devinette()