# Gribouillobot
<h3>Le bot détendu du week-end griboullis</h3>

<p>Chaque semaine, ce bot choisira un thème, cycliquement dans les catégories 'Arts' -> 'Naturel' -> 'Humains' ainsi que 6 mots au hasard. Tous ces mots ne pourront plus être tirés tant la catégorie en question comportera au moins 4 mots. (C'est le plus simple que j'ai trouvé)</p>

<h3>lexique.csv</h3>

<p>Ce fichier comporte tous les mots classés par catégorie, ainsi que le numéro de la semaine en cours. Il est fait pour être modifié, mais pas tant que ça :</p>

<ul><li>Le numéro de la semaine : modifiez juste le numéro, je pense que si vous mettez 'patate' à la place de 'semaine', ça va tout casser</li><li>Rajouter des mots : mettez les à la fin de la fin, en mettant une virgule avant, le programme s'occupera de trier le tout par ordre alphabétique</li></ul>

<h3>interface.py</h3>

<p>Pour l'instant un simple exemple qui prouve que ça marche ! Et pour montrer les fonctions aussi :</p>
<ul><li>choisir_theme()</li><li>choisir_mots()</li><li>sauvegarder_lexique()</li><li>reinitialiser_csv()</li><li>afficher_lexique()</li></ul>

<h3>core.py</h3>

Le truc qui fait le lien entre le csv et l'interface

<h4>class GribouillobotTirage:</h4>
<p>Permet de tirer au hasard les thèmes et les mots</p>
<p>__init__() : Paramètre obligatoire : Le fichier lexique</p>
<p>importer_lexique() : Parcourt le fichier et trie les mots dans un dictionnaire en fonction de la catégorie.</p>
<p>afficher_lexique() : Affique tout le lexique dans la console.</p>
<p>sauvegarder_lexique() : Réhabilite les mots s'il le faut, et recrée le fichier .csv dans l'ordre donné, en ajoutant les lignes de "commentaire" pour plus de lisibilité.</p>
<p>choisir_theme() : Choisis un thème dans une des trois catégorie. Une catégorie peut être spécifiée, mais sinon le choix se fait cycliquement.</p>
<p>choisir_mots() : Choisis N mots au hasard dans les catégories autorisées. Le paramètre 'tendu' permet de décider le nombre de mots tendus.</p>
<p>rehabiliter_mots() : Par défaut, parcourt les listes de mots et s'il y a 3 mots ou moins, rajoute les mots ignorés. 
En indiquant une categorie, seule celle-là sera réhabilitée.
En modifiant le seuil à 0, tous les mots ignorés seront rajoutés.
Cette fonction est appelée avant la sauvegarde, le processus est donc automatique.</p>
<p>reinitialiser_csv() : Remets tous les mots ignorés dans leurs listes principales respectives</p>