# Exo 2: Devine le nombre: Niveau 2
import random
"""
Reprend ton code pour le programme précédent. 
Modifie le pour donner seulement 3 chances à l'utilisateur pour deviner le nombre aléatoire choisit. 
Après 3 tentatives echouées, le programme s'arrête et affiche à l'utilisateur qu'il a épuisé ses chances.
"""


def devinette_niveau2():
    secret = random.randint(0, 100)  # Génère un nombre aléatoire entre 0 et 100 inclus
    tentatives = 3  # Nombre de tentatives autorisées

    for essai in range(tentatives):
        nbr_enter = int(input(f"Tentative {essai + 1}/{tentatives}: Devinez un nombre entre 0 et 100: "))

        if nbr_enter > secret:
            print("Trop grand")
        elif nbr_enter < secret:
            print("Trop petit")
        else:
            print("Exact! Vous avez trouvé le nombre.")
            return  # Sortie du programme si l'utilisateur devine correctement

    print(f"Vous avez épuisé vos {tentatives} tentatives. Le nombre secret était {secret}.")


# Appelle la fonction
devinette_niveau2()
