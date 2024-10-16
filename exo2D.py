"""
Exercice 2 : Devine le nombre (niveau difficile avec pénalité)
Écris un programme similaire où l'utilisateur commence avec un score de 100 points.
À chaque tentative incorrecte, il perd 10 points. S'il devine correctement avant de perdre tous ses points, le programme affiche le score final.
Le jeu s'arrête automatiquement après 3 tentatives ou si le score tombe à zéro.
"""

import random


def devinette():
    borne_inferieur = int(input("Entrer la bonne inferieur :"))
    borne_superieur = int(input("Entrer la bonne supérieure :"))

    tentatives = 3

    score = 100

    plage = random.randint(borne_inferieur, borne_superieur)

    for essai in range(tentatives):
        nbre_secret = int(
            input(
                f"Tentatives{essai + 1}/{tentatives} :Devinez le nombre entre {borne_inferieur} et {borne_superieur} : "
            )
        )
        if nbre_secret < plage:
            score -= 10
            print(f"Trop petit (Score: {score})")
        elif nbre_secret > plage:
            score -= 10
            print(f"Trop petit (Score: {score})")
        else:
            print(f"Exact! Vous avez trouvé le nombre. Votre score final est {score}.")

    print(
        f"Vous avez épuisé vos {tentatives} tentatives. Le nombre secret était {plage}."
    )


devinette()
