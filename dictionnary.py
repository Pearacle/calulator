"""
Consignes
1- Créez un dictionnaire appelé  fruits  avec les clés  pomme  ,  banane  et  orange  , et les valeurs  rouge  ,  jaune  et  orange  .
2- Ajoutez la clé  kiwi  avec la valeur  vert  au dictionnaire  fruits  .
3- Accédez à la valeur correspondant à la clé  banane  et stockez-la dans une variable appelée  couleur_banane  .
4- Modifiez la valeur associée à la clé  pomme  pour  vert  .
5- Supprimez la clé  banane  du dictionnaire  fruits  .
6- Affichez les clés restantes dans le dictionnaire."""

# Définition correcte du dictionnaire
fruits = {
    "pomme": "rouge",
    "banane": "jaune",
    "orange": "orange"
}

# Ajouter 'Kiwi' au dictionnaire existant
fruits['kiwi'] = "vert"

# Stocker la valeur de la clé "banane" dans une variable 
couleur_banane = fruits["banane"]

# Modifier la valeur associée à la clé pomme pour vert
fruits["pomme"] = "vert"

# Supprimer la clé banane du dictionnaire 
del fruits['banane']

# Afficher le dictionnaire modifié
print(fruits.keys())
print(fruits.values())
