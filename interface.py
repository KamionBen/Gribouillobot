from core import *

if __name__ == '__main__':

    bot = Gribouillobot('lexique.csv')  # Initialisation du bot
    print(f"-- Gribouillobot --\n - Version {VERSION} -\n\nSemaine {bot.semaine}\n")

    print("Le thème du jour :")
    print(f"• {bot.choisir_theme().upper()}")

    print("\nMots aléatoires :")
    liste_mots = bot.choisir_mots(tendu=0)
    print(f"• {' / '.join(liste_mots).upper()}")

    bot.sauvegarder_lexique()

    bot.reinitialiser_csv()  # Remets tous les mots ignorés dans les listes actives


