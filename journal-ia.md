# Intelligence Artificielle

## Introduction 

### Intelligence artificielle

Programmes visant à imiter les fonctions cognitives humaines

### Réseaux de neurones artificiels

Approche ayant pour but de concevoir une intelligence aritficielle 

### Exemples d'applications des réseaux de neurones artificiels

+ Voitures autonomes
+ Jeux de plateaux (e.g: morpions, echecs, ...) 
+ ***Reconnaissance d'images***
+ ...

### Matchbox AI 

Première tentative de réalisation d'une intelligence artificielle capable de jouer au jeu du moprion. Expérience réalisé dans les années 1960. Les machines de l'époque n'étant pas assez performantes, l'expérience est basé sur l'utilisation de boites d'alumette.

L'idée de base: Il est moins complexe de réaliser une intelligence artificelle qu'un programme capable d'anticiper toutes les possibilité du jeu, à condition que celle ci soit capable d'apprendre de ses expériences.

Voici comment fonctionne la machine: 

Il existe 304 état possible au jeu du morpion. On va donc prendre 304 boites d'allumettes sur lesquelles on va dessiner un état courrant du plateau pour une combinaison donnée. On va ensuite sur chaque emplacement vide qui représente une possibilité pour la machine de placer un X une couleur différentes.

Dans chaque boite on va placer des perles à quantité égale pour chaque couleur (ex: 5 perles rouges pour l'emplacement rouge). 

On va ensuite réaliser des parties. Pour chaque état du plateau on va prendre la boite qui correspond. On va tirer dans cette boite une perle au hasard et placer le X de la machine sur la couleur correspondant sur le plateau. 

La stratégie d'apprentissage est la suivante: 

+ Si le mouvement effectué mène à la défaite de la machine, alors on va diminuer la quantité de perle de la couleur de celle qui a mené à la défaite. On va donc réduire la probabilité que la machine fasse de nouveau ce choix. On pénalise donc cette décision. 
+ Si le mouvement effectué mène à la victoire de la machine, alors on va augmenter la quantité de perle de la couleur de celle qui a mené à la victoire. On va donc augmenté la probabilité que la machine fasse de nouveau ce choix. On récompense donc cette décision. 
+ Si le mouvement effectué mène à la égalité alors on va augmenter la quantité de perle de la couleur de celle qui a mené à l'égalité. Cependant on va le faire dans une moindre mesure que lors de la victoire car on va préférer la victoire à l'égalité.

Voici donc le premier exemple basique de machine intelligente dans l'histoire de l'humanité. 

### La stratégie des réseaux de neurones artificiels

Le concept d'apprentissage, c'est à dire au cours des expérience de la machine on va récompenser les décisions qui aboutissent au resultat attendu et sanctionner les décisions qui ne mènent pas au resultat attendu. 

## Computer vision 

Pour concevoir un réseau de neuronnes artificiels capable de reconnaitre des éléments visuels sur une image il est important de conceptualiser et comprendre la manière donc un ordinateur se représente une image et ce qui la différencie de la façon dont les humains le font.

### La manière donc un ordinateur se représente une image

Une machine se représente une image sous la forme d'une suite de nombres. 

### Quelles sont les deux caractéristiques de la visions humaines. 


