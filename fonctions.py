"""Créez une fonction appelée  salaire_mensuel(salaire_annuel)  qui prend en paramètre un salaire annuel et retourne le salaire mensuel 
correspondant en divisant le salaire annuel par 12.

Créez une fonction appelée  salaire_hebdomadaire(salaire_mensuel)  qui prend en paramètre un salaire mensuel et retourne le salaire 
hebdomadaire correspondant en divisant le salaire mensuel par 4.

Créez une fonction appelée  salaire_horaire(salaire_hebdomadaire, heures_travaillees)  qui prend en paramètres un salaire hebdomadaire 
et le nombre d'heures travaillées par semaine, et retourne le salaire horaire correspondant en divisant le salaire hebdomadaire par 
le nombre d'heures travaillées par semaine.

Demandez à l'utilisateur de saisir son salaire annuel.

Demandez à l'utilisateur de saisir le nombre d'heures travaillées par semaine.

Appelez les fonctions précédemment créées pour calculer le salaire horaire correspondant.

Affichez le résultat sous la forme : "Votre salaire horaire est de XX euros"."""


# Créer une fonction salaire_mensuel avec un paramètre salaire_annuel
def salaire_mensuel(salaire_annuel):
    return salaire_annuel / 12

# Créer une fonction salaire_hebdomadaire avec paramètre un salaire mensuel qui retourne le salaire hebdomadaire
def salaire_hebdomadaire(salaire_mensuel):
    return salaire_mensuel / 4

# Créer une fonction salaire_horaire avec paramètre salaire_hebdomadaire, heures_travaillees qui retourne le salaire horaire
def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    return salaire_hebdomadaire / heures_travaillees

# Exemple d'utilisation
salaire_annuel = int(input("Entrer votre salaire annuel: "))
heure_travail = int(input("Entrer le nombre d'heures travaillées par semaine: "))
salaire_mensuel_value = salaire_mensuel(salaire_annuel)
salaire_hebdo = salaire_hebdomadaire(salaire_mensuel_value)
salaire_heure = salaire_horaire(salaire_hebdo, heure_travail )


print(f"Votre salaire horaire est de {salaire_heure} euros")
