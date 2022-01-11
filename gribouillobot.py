
### GRIBOUILLOBOT - random thèmes & sujets ###
import random
 
 
# GÉNÉRATEUR À GRAINES D'IDÉES - VERSION ALPHA
# Thèmes monde naturel/Monde humain - mots tendus/détendus

### FAIRE TOURNER TEL QUEL OU AGIR AUX POINTS ALPHA (en fin de code)
  
###Lexique
"""
LISTES FINALES
THÈMES

techniques[] = thèmes techniques
cultures[] = thèmes cultures

espN[] = Espace naturel
espH[] = Espace humain
tpsN[] = Temps naturel
climat[] = Temps climatique
tpsH[] = Temps humain
histoire[] = Temps historique

MOTS
obT[] = Objets tendus
oBD[] = Objets détendus
etT[] = États tendus
etD[] = États détendus
anT[] = Animaux tendus (prédateurs, dangereux...)
anD[] = Animaux détendus (proies, enfants...)

LISTES DE LISTES
THEMES
allthemes[] = tous les themes
themesA[] = thèmes arts
themesN[] = thèmes naturel
themesH[] = thèmes humain

MOTS
allM = tous les types de mots
allT = tous les mots tendus
allD = tous les mots détendus
allOb = tous les objets
allEt = tous les états
allAn= tous les animaux
"""

### Listes lexiques 

####################################################
### THEMES (xxxN = xxx Naturel / xxxH = xxx Humain )


### Arts
techniques = ["ombre","lumière","couleur","perspectives","contraste","épaisseur","profondeur","figuration","nature-morte","nature-vive","abstrait","caricature","manga","comics","belge","architecture","portrait","cubisme","art-nouveau","art-déco","pointillisme","surréalisme"]

cultures = ["cinema","musique","science-fiction","fantasy","classique","Steam-punk","Cyber-punk","télévision","internet","meme","super-héros","industrie","hollywood","bollywood","nollywood"]


### Espace Naturel
espN = ["jungle","savane","montagne","plaine","steppe","lande","forêt","antarctique","marais",
"mangrove","désert","mer","océan","littoral","espace","tropiques","îles","collines"] 

### Espace Humain
espH = ["ville","banlieue","foyer","cuisine","bureau","café","Bar","restaurant","commerce","lit","chambre","parc d'attraction","parc"]


### Temps Naturel
tpsN =["hiver","printemps","été","automne","aube","matin","zenith","midi","après-midi","soirée","crépuscule","nuit","nadir","marée haute","marée basse","equinoxe","solstice"]

climat = ["pluie","tempête","ouragan","typhon","orage","mousson","saison sèche","éclaircie","rayon de soleil","nuageux","caniculaire","vents","blizzard"]

### Temps Humain
tpsH = ["fêtes","traditions","rites","carnaval","naissance","mort","récoltes","diplômes","mariage","enfance","adolescence","maturité","vieillesse","grand-âge","enterrement","jeux","repos","travaux"]

histoire = ["Dinosaures","préhistoire","age de pierre/bronze","antiquité","médiéval","renaissance","moderne"]



##################################################
### MOTS (xxT = xx tendu / xxD =  xx détendu)

### Objets 
obT = ["virus","éclair","finance","travail","ténèbres","vice","tension","prise","bureau","pince","outils","machine","chronomètre","arme","nuage","monnaie","ruine","vent","pluie","dette","neige","devoir"]
obD = ["bonbon","soleil","plante","caramel","élastique","mousse","doudou","sieste","méditation","chatouille","calin","caresse","copains","copines","papouilles","turlututu","carnaval","fruit"]


#### États  
etT = ["depressif","angoisse","noir","tendu","gris","mort","électrique","électronique","précipité","problème","squeezé","cassé","vénère","maladie","handicap","effondré","mouillé","flotte","déséquilibré","aiguë","pointu","punk"]
etD = ["rigolo","chaud","doux","moelleux","mou","rond","relax","détendu","calme","zen","gentil","amoureux","balancé","au-poil","nickel","confort","apaisé","ronflant","dormant","berçant"]

### Animaux 
anT = ["insecte","tigre","araignée","larve","loup","rapace","requin","murène","anguille","dragon","crocodile","monstre","vélociraptor","tyranosaurus rex"]
anD = ["otarie","escargot","chaton","giraffe","rhinoceros","pingouin","canari","chiot","chenille","papillon","panda","ourson","renard","zébu","vache","chèvre"]





###############################################
### LISTES GROUPÉES 


### liste thèmes ###
#all thèmes (tous) 
allthemes = [techniques,cultures,espH,tpsH,histoire,espN,tpsN,climat]
#thèmes arts
themesA = [techniques,cultures]
#thèmes humains
themesH = [cultures,espH,tpsH,histoire]
#thèmes naturels
themesN = [espN,tpsN,climat]

#############################
###Listes mots ###
#all mots
allM = [obT,etT,anT,obD,etD,anD]
#all tendus
allT = [obT,etT,anT]
#all détendus
allD = [obD,etD,anD]
#all objets
allOb = [obT,obD]
#all états
allEt = [etT,etD]
#all animaux
allAn = [anT,anD]
################################################


#################################
### METHODES À DÉFINIR ###
### içi mode automatique en agissant directement dans le code, suivre ALPHA pour voir où agir

##############
### THEMES ###
##############

### tire un thème complètement aléatoire ###
#tire un type de thème au hasard
random_theme = random.choice(allthemes)  ### ALPHA  : içi changer la liste 'allthemes' par une liste de liste (ex: 'themesA')
# tire un thème au hasard dans le type tiré
random_hasard = random.choice(random_theme) ### ALPHA  : içi changer 'random_theme' par une liste (ex: "tpsH" 


### tire un thème ARTS tous les troix tirages ###
#à développer


############
### MOTS ###
############
### tire six mots complètement aléatoires ###
nbmots = 6
i = 0
sixmots = ""
while i < nbmots:

	random_td = random.choice(allM)   ### ALPHA  : içi changer la liste 'allM' par une liste de listes (ex : 'allD' )
	random_mot = random.choice(random_td) ### ALPHA : içi changer 'random_td' par une liste finale (ex: 'anD')
	sixmots = sixmots+" "+random_mot+" "+"/"
	i+=1

### tire 3 couples de mots 
# à développer












###DEBUT
################
###INTERFACE CONSOLE ###
#ACCEUIL
print("\n")
print("GRIBOUILLOBOT - générateur à graines d'idées ")
print("\n")
################
#MENU / CHOIX ALL ALÉATOIRES / CHOIX 2 / ... / QUITTER ###
################
#RESULTAT -> RE-TIRER / RETOUR MENU / QUITTER ###

print('Thèmes et sujets générés :\n')
### print thème aléatoire
print('Thème aléatoire : ',random_hasard)	
#print six mots aléatoires
print("Six mots au hasard: "+sixmots)
################


print('\n')
###FIN













