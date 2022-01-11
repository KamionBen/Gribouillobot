import csv
from random import choice, shuffle

VERSION = "0.1.3"


class Gribouillobot:
    def __init__(self, fichier):
        """ Charge le fichier donné et classe les mots dans un dict selon les catégories """
        """ Chaque catégorie a une liste "_ignore" associée pour stocker les mots utilisés récemment """
        """ Thèmes """
        # Tous : techniques, cultures, espace_naturel, espace_humain, temps_naturel, temps_humain, climat, histoire
        # Thèmes art : techniques, cultures
        # Thèmes humains : cultures, espace_humain, temps_humain, histoire
        # Thèmes naturels : espace_naturel, temps_naturel, climat
        """ Mots """
        # Tous : objets_tendus, objets_détendus, états_tendus, états_détendus, animaux_tendus, animaux_détendus
        # Mots tendus : objets_tendus, états_tendus, animaux_tendus
        # Mots détendus : objets_détendus, états_détendus, animaux_détendus
        # Objets : objets_tendus, objets_détendus
        # Etats : états_tendus, états_détendus
        # Animaux : animaux_tendus, animaux_détendus

        self.fichier = fichier  # Pour que la fonction importer_lexique() fonctionne
        self.semaine, self.lexique = self.importer_lexique()  # Par commodité, la variable semaine est stockée avec le lexique

    def importer_lexique(self):
        """ Charge le fichier .csv et renvoie un dictionnaire"""
        with open(self.fichier, newline='') as csvfile:
            reader = csv.reader(csvfile)
            semaine = None
            lexique = {}
            for row in reader:
                title = row[0]
                if title == 'semaine':
                    semaine = int(row[1])
                elif title[0] == "#":
                    pass
                else:
                    lexique[title] = sorted(row[1:])
        return semaine, lexique

    def afficher_lexique(self):
        """ Affiche toutes les listes du lexique dans la console """
        for key, value in self.lexique.items():
            print(f"{key}:    {value}")

    def sauvegarder_lexique(self):
        """ Fais les opérations de fin et sauvegarde le lexique """
        # TODO : Ne fonctionne pas encore
        """ Opérations : semaine += 1, réhabiliter les mots qu'il faut, trier les listes """
        """ Penser à rajouter les '#' pour la lisibilité """
        self.semaine += 1
        themes_liste = ['techniques', 'cultures', 'espace_naturel', 'espace_humain',
                        'temps_naturel', 'temps_humain', 'climat', 'histoire']

        for theme in themes_liste:
            new_list = self.lexique[theme].copy()
            ignore_list = self.lexique[f"{theme}_ignore"].copy()
            if len(new_list) == 0:  # La liste est vide, on la rerempli
                new_list = ignore_list.copy()
                ignore_list = []

            new_list.sort()
            new_list.insert(0, theme)
            ignore_list.insert(0, f"{theme}_ignore")

            print(new_list)
            print(ignore_list)

    def choisir_theme(self, categorie=None):
        """ Choisis un thème dans la catégorie donnée """
        """ Si aucune catégorie n'est donnée, continue le cycle Arts -> Naturel -> Humains """
        cycle = ['Arts', 'Naturel', 'Humains']
        if categorie is None:
            categorie = cycle[self.semaine % len(cycle)]

        choix = None
        if categorie == 'Arts':
            choix = choice(('techniques', 'cultures'))
        elif categorie == 'Naturel':
            choix = choice(('espace_naturel', 'temps_naturel', 'climat'))
        elif categorie == 'Humains':
            choix = choice(('cultures', 'espace_humain', 'temps_humain', 'histoire'))
        else:
            raise TypeError(f"La catégorie entrée, '{categorie}', n'est pas valide")

        shuffle(self.lexique[choix])  # On mélange le paquet de mots
        selection = self.lexique[choix].pop(0)  # On retire le premier
        self.lexique[f"{choix}_ignore"].append(selection)  # On ajoute le mot à la liste des mots ignorés

        return selection

    def choisir_mots(self, compte=6, sauf=None, seulement=None, equilibre=False):
        """ Choisis N mots au hasard dans les catégories autorisées """
        # Toutes les catégories pour l'instant
        categories_autorisees = ['objets_tendus', 'objets_détendus', 'états_tendus',
                                 'états_détendus', 'animaux_tendus', 'animaux_détendus']

        liste_mots = []
        while len(liste_mots) < compte:
            categorie_choisie = choice(categories_autorisees)
            shuffle(self.lexique[categorie_choisie])  # On mélange le paquet
            mot_choisi = self.lexique[categorie_choisie].pop(0)  # On retire le premier mot
            self.lexique[f"{categorie_choisie}_ignore"].append(mot_choisi)  # On le met dans la liste '_ignore'
            liste_mots.append(mot_choisi)

        return liste_mots


if __name__ == '__main__':
    """ Cette partie de code se trouverait plutôt dans un fichier interface.py """
    bot = Gribouillobot('lexique.csv')  # Initialisation du bot
    print(f"-- Gribouillobot --\n - Version {VERSION} -\n\nSemaine {bot.semaine}\n")

    print("Le thème du jour :")
    print(f"• {bot.choisir_theme().upper()}")
    print("\nMots aléatoires :")
    liste_mots = bot.choisir_mots()
    affichage = "• "
    first = True
    for mot in liste_mots:
        if first:
            affichage += mot.upper()
            first = False
        else:
            affichage += f" / {mot.upper()}"
    print(affichage)
    #print("\nAffichage du lexique :")
    #bot.afficher_lexique()  # On voit que le thème choisi apparaît bien dans la liste "_ignore"

    print("\nTest de la sauvegarde :")
    bot.sauvegarder_lexique()



