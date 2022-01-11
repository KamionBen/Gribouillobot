import csv

VERSION = "0.1.1"

""" Cette version ne fait rien d'autre qu'afficher le lexique """
""" Pas en convaincu par ce système, peut-être utiliser une classe pour le lexique ? """


def importer_lexique(fichier):
    """ Charge le fichier .csv et renvoie un dictionnaire"""
    with open(fichier, newline='') as csvfile:
        reader = csv.reader(csvfile)
        semaine = None
        lexique = {}
        for row in reader:
            title = row[0]
            if title == 'semaine':
                semaine = row[1]
            elif title[0] == "#":
                pass
            else:
                lexique[title] = sorted(row[1:])
    return semaine, lexique


def sauvegarder_lexique(fichier, sort=True):
    """ Sauvegarde le lexique et trie les listes par ordre alphabétiques (ou pas) """
    # TODO


def choisir_theme(lexique, categorie=None):
    """ Renvoie un thème au hasard, si aucune catégorie n'est donnée, choisit au hasard """
    # Le thème choisi est retiré de la liste principale et ajouté à la liste "_ignore" correspondante
    # TODO


def choisir_mots(lexique, nombre=6, categorie=None):
    """ Renvoie une liste de six mots, si aucune catégorie n'est donnée, choisit au hasard """
    # Les mots choisis sont retirés de leur listes principales respective
    # et ajoutés aux listes "_ignore" correspondantes
    # TODO


def rehabiliter_theme(lexique, temps=8):
    """ Vérifie les listes "_ignore", et remets les thèmes dans la liste principale
    s'ils sont ignorés depuis plus longtemps que la variable 'temps' (8 semaines par défaut) """
    # ATTENTION : Pour le décompte, il faudra sûrement ajouter une None à chaque liste inutilisée
    # Todo


def rehabiliter_mots(lexique, temps=8):
    """ Vérifie les listes "_ignore", et remets les mots dans la liste principale
    s'ils sont ignorés depuis plus longtemps que la variable 'temps' (8 semaines par défaut) """
    # ATTENTION : Pour le décompte, il faudra sûrement ajouter une None à chaque liste inutilisée
    # Todo


def print_lexique(lexique):
    for key, value in lexique.items():
        print(f"{key}:    {value}")


if __name__ == '__main__':
    semaine, lexique = importer_lexique('lexique.csv')

    print(f"Gribouillobot v{VERSION}\n-- Semaine n°{semaine}\n")
    print_lexique(lexique)


