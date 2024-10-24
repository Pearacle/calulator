"""Demandez à l'utilisateur de saisir une liste de nombres séparés par des virgules (par exemple : 1,2,3,4), et affichez cette liste.

Calculez et affichez la somme des nombres dans la liste.

Calculez et affichez la moyenne des nombres dans la liste.

Calculez et affichez le nombre de nombres dans la liste qui sont supérieurs à la moyenne.

Calculez et affichez le nombre de nombres dans la liste qui sont pairs."""

# créer une liste vide
liste_nbr: list[int] = []

# Déclarer une variable pour stocker les nombres entré par l'utilisateur
input_string = input("Entrez des nombres séparés par des virgules (exemple: 1, 2, 3, 4): ")

# Créer une nouvelle liste où chaque élément de la liste résultante est converti en entier
liste_nbr = [int(nbr) for nbr in input_string.split(",")]

# Afficher la liste
print(input_string)

# Calcul et affichage de la somme des nombres dans la liste
somme = sum(liste_nbr)
print(somme)

# Calcul et affichage de la moyenne des nombres de la liste
moyenne = somme / len(liste_nbr)
print(moyenne)

# Calcul et affichage du nombre de nombres dans la liste qui sont supérieurs à la moyenne.
nbr_elem: list[int] = []
for elem in liste_nbr:
    if elem > moyenne:
        nbr_elem.append(elem)

print(nbr_elem)

# Calcul et affichage du le nombre de nombres dans la liste qui sont pairs.
nbr_pairs = 0
for elem in liste_nbr:
    if elem % 2 == 0:  # Check if the number is even
        nbr_pairs += 1  # Increment the even number counter

print(nbr_pairs)
