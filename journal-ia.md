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

+ Comparaison/Correspondance entre l'information visuelle et un dictionnaire interne crée au cours de l'expérience de l'individus
+ Déduction et conceptualisation en fonction du context dans lequel se trouve l'élément visuel 

Le second point étant la cause d'un défaut de la vision humaine: L'effet d'optique

### A quel problème majeur est confronté une machine pour reconnaitre une image ?

Un ordinateur se répésente une image comme un ensemble de pixel, valeurs numériques dans une liste. Le problème étant que chaque valeur numérique représente l'intessité lumineuse d'un point (pixel) de l'image. Donc si l'ordinateur se base sur cette suite de valeur pour comparer un même objet sous une instensité lumineuse différente alors il va conclure que se sont deux objects différents. 

Pour se faire la machine va utiliser des alogirthimes permettant de donner à chaque pixel une valeur indépendante de l'intensité lumineuse en comparant chaque pixel à son voisin et en attribuant à chaque pixel la différences absolue de valeur entre ce pixel et son voisin. C'est ce qu'on appelle les algorithms de vertical et horizontal filter. 

## Simply Shape Image recognition task 

Dans ce premier exemple basique nous allons développer un alogorithm capable de reconnaitre une forme géométrique sur une image. 

### Dataset 

Le dataset est un ensemble de donnée qui va regrouper l'ensemble d'image de forme différentes sur lesquelles on va tester notre algorithm. Chaque image consiste en une grille de 20*20 pixels. 

### Quels critère va nous permettre de différencier une forme d'une autre ?

Entre un cercle, un triangle et un carré, c'est le nombre d'angle qui va nous permettre de faire la différence entre une forme et une autre. 

### Sur quel critère se baser pour détecter une forme ? 

On part du principe que nos image sont des images binaires (pixel blanc ou noir). Les pixels noirs décrivent notre forme. 

On pourrait d'abord penser à étudier chaque pixel (mesure locale) et compter le nomlbre de ses voisins pour déterminer si c'est un angle ou non (<= 3). Cependant ce critère n'est pas assez pertinant et peu mener à de mauvais résultat (ex: le triangle). 

On va donc se baser sur le critère suivant: 

On va imaginer que le tracé de pixel noir qui décrit notre forme est un chemin. On va suivre alors ce chemin comme si on était on était équipé d'une bousole. On va alors détecter si il y'a un changement de direction dans le chemin (ex: S => W). 

On va ensuite calculer la valeur de l'angle autour duquel se fait le changement de direction (ex: tourner à 90°). Si ce changement de direction s'est effectué avec un angle plus grand ou égal à 90°, alors on est dans le cas d'un angle pour la forme étudié. 

Pour se faire on va devoir réaliser un algorithme permettant de définir la frontière de la shape (en terme de chemin de pixel). On va ensuite passer d'un pixel à un autre le long de cette frontière. On va a chaque passage d'un pixel à l'autre faire passer une fleche qui va du centre du pixel précédent au suivant. On va comparer cette direction à la précédente. Si le changement de direction est supérieur ou égal à 90° c'est un angle.

Le problème réside dans la création de ce chemin de pixel. On va découvrir des edges cases à chaque fois et modifier l'alogorithm permettant une création de frontière optimale. 

### Quel est le problème d'une apporche algorithmique pour résoudre cette tâche ? 

Le problème est qu'il bien trop complexe de pouvoir écrire un programme qui anticipe tous les edge cases qui peuvent survenir dans l'analyse d'un datastet volumineux. De puis si on change le dataset en ajoutant de nouvelles formes, alors il va falloir tester de nouvaux notre algorithme sur ces nouvelles images, détecter les nouveaux edges cases et adapter à nouvaux notre algorithme pour ces cas partoculier etc. 

On se rend vite compte qu'il est impossible de réaliser un tel programme qui va se complexifier et être immaintenable pour un humain. 

## Réseaux de neuronnes 

### Quelles est la différence entre une approche machine basé sur l'algorithm et une intelligence naturelle/artificielle ?

La différence fondamentale réside dans la fléxibilité. Une approche algorithmique nous fait tomber dans un labyrith de conditions spéciale et de edge case complexe.

## Quelle est la particularité du cerveau humain ? 

Il apprend de l'experience. 

## Quels sont les deux principes fondamentaux d'un neuronne artificiel ? 

+ Un neurone artificiel suit des règles logique de façon mécanique qui à partir de certains inputs amène à un certain output 
+ Un neurone artificiel peut à partir des même inputs, amener à un output différents si on change sa configuration interne

## Binary neurons 

Les neurones binaires fonctionnent de la façon suivante: 

+ Ils ne peuvent avoir comme valeur de sortie (output) seulement deux état: ``òn```/ ```off```.

Pour décider à quel état est l'output, ils décident de la façon suivante: 

+ Ils additionnent la valeur de chacun des inputs;
+ Ils comparent cette somme à la valeur "curseur" qui est paramêtrer dans leur configutation;
+ Si la somme des inputs est inférieur à la valeur curseur, alors l'état de sortie est à ```off```;
+ Si la somme des inputs est supérieur à la valeur curseur, alors l'état de sortie est à ```on```;


