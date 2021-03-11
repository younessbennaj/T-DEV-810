# T-DEV-810 

## Objectif du TP

Mettre en place ***un réseau de neurone artificiel*** capable de reconnaitre un ***chiffre*** (integer) compris entre ***0 et 9***.

# Introduction aux ANNs

## Definitions des concepts de base

### Intelligence aritficielle 

Programme qui a pour but d'imiter les fonctions cognitives humaines. Comme l'intelligence naturelle (ex: humaine), elle est basé sur la fléxibilité, c'est à dire la capacité de l'intelligence à apprendre des ses experiences.

### Neurone artificiel 

Entité logique (porte logique) basé sur deux principes fondamentaux: 

+ Un neurone artificiel suit des règles logiques, qui lui sont propres, de façon à donner un certain output à partir des certains inputs. 
+ Un neurone artificiel peut à partir des mêmes inputs, mener à un output différent si on change son configuration interne.

Les neurones aritificel sont les "briques élémentaires" qui contituent les ANNs. Ils fonctionnent sur le principe de porte logique. C'est à dire qu'ils ont une logique interne, et en fonction des inputs reçu on va avoir un certain output. 

e.g: Neurone artificiel basé sur la porte logique AND

```
 Input1 = 0;
 Input2 = 1;
 
 AN Logic => Input1 AND Input2 
 
 AN Output = Input1 && Input2 = 0
```

Un neurone artificiel, est une entité fléxible, c'est à dire qu'il peut ensuite mettre à jour son mécanisme interne, c'est à dire modifier les règles logique qu'il suit en interne:

e.g: Neurone artificiel basé sur la porte logique OR

```
 Input1 = 0;
 Input2 = 1;
 
 AN Logic => Input1 OR Input2 
 
 AN Output = Input1 && Input2 = 1
```

C'est grâce à ce mécanisme basique qu'un ANN peut être ***fléxible*** et ***apprendre de ses expériences***.

### Un réseau de neurone artificiel (ANN)

C'est une approche visant à créer une intelligence artificielle. Un ANN apprend à résoudre des problèmes comme le ferait un cerveau humain.

Cette approche est est basé sur la mise en relation de neurones artificiels sous forme de couche lié les unes aux autres. L'output des neurones situé dans les couches inférieures sont l'input des neuronnes des couches supérieurs. 

L'avantage d'un réseau de neurone artificiel c'est qu'il apprends de ses expériences.

### Apprentissage d'un ANN 

Un ANN apprends de ses expériences via ce qu'on appelle un entraintement ou 'training phase' en anglais. Lors de cette phase d'entraintement, l'ANN va être soumis à un dataset qui représente un ensemble d'information que l'ANN doit pouvoir reconnaitre grâce à sa configuration interne. 

Si l'ANN reconnait bien l'information, alors il ne se passe rien. 

Si l'ANN ne reconnait pas l'information, alors sa configuration interne est mise à jour pour qu'il ait plus de chance de reconnaitre l'information la prochaine dois. 

### Image recognition 

Programme visant à faire reconnaitre, par une machine, une information visuelle à partir d'une image donnée. La compléxité tiens à la fois dans les différences entre les fondements de la vision humaine et de celle des machines, mais également dans le manque de flexibilité d'une approche algoritmique classique pour résoudre ce problème. C'est pour cela qu'on utilise une approche utilisant les intelligence aritificielle, flexible par nature. 

### Algorithmes de vision machine 

Programme visant à traiter en amont une image pour qu'elle puisse être utilisé correctement par une machine. Cela s'appuie sur les caractéristiques de la vision machine: Interprétation d'une image sous forme d'une liste de valeur numérique (intensité en nuance de gris d'un pixel de l'image). 

# Le neurone artificiel en détail


# Bootstrap

## Dataset

Le dataset est composé de 60000 images représentant un chiffre compris entre 0 et 9. Ces images sont composé d'une grille de 28*28 pixel. Chacun de ces pixels représente une nuances de gris. La nuance la plus forte indique l'objet à étudier. 

Les pixels sont réprésenté par la machine sous la forme d'une valeur numérique, représentant la nuance de gris corresponsante à ce pixel. L'image pour la machine est donc représenté sous la forme d'un ensemble de valeur numériques.

La coordonnées [10,12,14] représente le pixel de la ligne 12, à la colonne 14, de la 10ème image. 

### Objectif et rôle 

Dans le cas d'une intelligence artificielle de reconnaissance d'images, l'objectif d'un dataset est d'entrainer un réseau de neurone à reconnaitre une information visuelle.

### Le mécanisme d'apprentissage

L'entrainement de notre ANN va consisiter à soumettre ce dernier à notre dataset et tenter de lui faire reconnaitre les chiffres de 0 à 9 sur les images qui composent celui ci.

A chaque image notre ANN va faire de son mieux pour reconnaitre le chiffre sur l'image. Si il réussi, alors il ne se passe rien. 

Si par contre notre ANN ne reconnait pas le chiffre, alors sa mécanique en interne va être modifié pour qu'il ait plus de chance de reconnaitre le chiffre la prochaine fois.

## MNIST, Python et les librairies

### MNIST 

C'est un dataset, c'est à dire une collection d'image, représentant des chiffres écrit à la main. C'est un dataset très utilisé pour entrainer des réseaux de neurones articifiel à traité et reconnaitre des chiffres sur une image. 

Il va être conçu de la façon suivante: 

- 1 tableau de 60000 élément qui représente notre échantillon d'image 
- Chaque élément du tableau est un tableau qui contient 28 listes représetant les lignes en pixel de chaque image

Les dimensions du tableau sont donc: ```(60000, 28, 28)```

### Notebook Jupyter 

C'est une interface qui va nous permettre de présenter le travail effectuer en combinant language naturel et language informatique. Cela va nous permettre de faire à la fois un travail de rédaction écrit en language humain, et ajouter du code live, de faire de la visualisation de de donnée. 

### Python 

Language de programmation machine utilisé pour réalisé nos programmes. 

### pip 

```pip``` est le gestionnaire de package/librairie du langage python, il va nous permettre de pouvoir importer des librairie python externe sur notre machine.

### Tenserflow 

Librairie de machine learning écrite en Python. Elle va nous permettre de créer, d'entrainer et de tester notre réseau de neurones artificiels. 

### Maptolib 

Librairie python qui va nous permettre de réalisé des statistiques et des graphs de données dans le but de présenter des informations comme la distribution de chaque chiffre dans le dataset par exemple. 

### Numpy 

Librairie python qui nous permet de travailler avec des tableaux à plusieurs dimensions. Cela va nous être utile pour notre dataset qui représente l'échantillon d'image sous la forme d'un tableau à 3 dimension. 

### requirement.txt 

On va pouvoir ajouter donc la liste de nos dépendances, c'est à dire les librairies dont vont dépendre notre projet, dans un fichier dédié: 

```
# requirement.txt
tenserflow
maptolib
numpy
```

et pour les installer il suffit de lancer la commande 

```
pip3 install -r requirement.txt
```

## Structure du projet 

```main.py``` est le fichier principal de notre projet. 

```
main.py
```
## Les 3 modes d'un programme d'ANN 

```train```: On va entrainer le réseau de neurone artificiel à partir du dataset. 

```test```: On va tester le réseau de neurone. 

```use```: On va utiliser le réseau de neurone sur des nouvelles images de chiffre. 







