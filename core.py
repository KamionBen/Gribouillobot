import csv
from random import choice, shuffle

VERSION = "1.0"


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

        self.semaine += 1
        self.rehabiliter_mots()  # Réhabilitation par défaut
        themes_liste = ['techniques', 'cultures', 'espace_naturel', 'espace_humain',
                        'temps_naturel', 'temps_humain', 'climat', 'histoire']
        mots_liste = ['objets_tendus', 'objets_détendus', 'états_tendus',
                      'états_détendus', 'animaux_tendus', 'animaux_détendus']
        with open(self.fichier, 'w', newline='') as fichier:
            writer = csv.writer(fichier, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)

            writer.writerows([['semaine', self.semaine], ['#THEMES']])
            for theme in themes_liste:
                writer.writerow(['#'])  # Pour la visibilité
                new_liste = [theme] + self.lexique[theme]
                ignore_liste = [f"{theme}_ignore"] + self.lexique[f"{theme}_ignore"]
                writer.writerows([new_liste, ignore_liste])

            writer.writerow(['#MOTS'])
            for mot in mots_liste:
                writer.writerow(['#'])  # Pour la visibilité
                new_liste = [mot] + self.lexique[mot]
                ignore_liste = [f"{mot}_ignore"] + self.lexique[f"{mot}_ignore"]
                writer.writerows([new_liste, ignore_liste])

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
        self.lexique[choix].sort()  # On refait le tri

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
            self.lexique[categorie_choisie].sort()  # On refait le tri

        return liste_mots

    def rehabiliter_mots(self, categorie=None, seuil=3):
        """ Par défaut, parcourt les listes de mots et s'il y a 3 mots ou moins, rajoute les mots ignorés """
        """ En indiquant une categorie, seule celle-là sera réhabilitée """
        """ En modifiant le seuil à 0, tous les mots ignorés seront rajoutés """
        """ Cette fonction est appelée avant la sauvegarde, le processus est donc automatique"""
        if seuil < 0:
            raise ValueError(f"La valeur seuil ne doit pas être inférieure à zéro")
        elif categorie is None:
            for index in ['techniques', 'cultures', 'espace_naturel', 'espace_humain', 'temps_naturel', 'temps_humain',
                          'climat', 'histoire','objets_tendus', 'objets_détendus', 'états_tendus', 'états_détendus',
                          'animaux_tendus', 'animaux_détendus']:
                if seuil == 0 or len(self.lexique[index]) <= 3:
                    """ Réhabilitation """
                    self.lexique[index] += self.lexique[f"{index}_ignore"]  # On fusionne les listes
                    self.lexique[index].sort()  # On trie la liste principale
                    self.lexique[f"{index}_ignore"] = []  # On vide la liste _ignore
        else:
            """ Réhabilitation spécifique """
            # Renverra une erreur si la catégorie est mal orthographiée, attention
            self.lexique[categorie] += self.lexique[f"{categorie}_ignore"]  # On fusionne les listes
            self.lexique[categorie].sort()  # On trie la liste principale
            self.lexique[f"{categorie}_ignore"] = []  # On vide la liste _ignore

    def reinitialiser_csv(self):
        self.rehabiliter_mots(seuil=0)
        self.sauvegarder_lexique()





