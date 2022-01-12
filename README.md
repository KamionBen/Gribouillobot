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