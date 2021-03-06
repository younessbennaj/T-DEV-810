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

### Neurone Artificiel Binaire 

***

##### Résumé 1

Un neurone artificiel binaire est une entité qui en fonction de deux inputs en entré, peut être actif ou inactif en output. 

L'état de sorti est déterminé par la configuration interne du neurone artificiel. Cette configuration est basé sur la decision boundary qui est la valeur qui détermine si en fonction de la valeur totale des inputs, l'output est actif ou inactif. 

```
I1 + I2 >= b ?
```

Chaque input peut se voir attribuer un poids 'input weight' qui va permettre de jouer sur la slope de la decision boudary (voir représentation graphique), tel que:

```
I1 * w1 + I2 * w2 >= b ?
```

Un neurone artificiel agit donc comme une porte logique: En fonction de 2 inputs il donne un certain input. 

Cependant on peut vite se rendre compte qu'avec neurone artificiel on peut seulement concevoir une porte OR ou AND. 

Pour les portes logiques plus complexe on va donc recourir à la supérposition en couche des neurones. Cela va nous permettre de faire en sorte que certains neurone soit les inputs des neurones des couches supérieurs. 

***

##### Résumé 2

Un neurone artificiel binaire, est un neurone artificiel qui dépend de 2 input pour déterminer son output. Chaque input en entrée possède une certaine valeur qu'on va appeler ***I1*** et ***I2***.

La logique interne d'un neurone binaire repose sur ce qu'on appelle la ***decision boudary***, une valeur limite que l'on nomme ***b***. 

Voici un exemple de logique d'un neurone binaire:

L'output (0 ou 1) de ce neurone binaire est determiné de la façon suivante: Si la valeur totale des deux inputs cummulé est supérieur ou égale à la valeur limite, alors l'output est à 1 sinon il est à 0 (pas de signal). On peut résumé cela par la formule: 

```
I1 + I2 >= b
```

Il existe d'autres types de logique interne (ou "slope") pour un neurone binaire.

eg:

```
I2 - I1 >= b
``` 

Cette logique interne determine le comportement comme porte logique d'un neurone artificiel. 

La capacité d'apprentissage et de prédiction d'un neurone articifiel (et donc d'un ANN) repose sur le principe suivant: Déterminer la valeur optimale de la ***decision boudary*** et optmiser sa logique interne (changer la "slope"/"pente" d'une ***decision boudary***). 

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

Librairie de deep learning écrite en Python. Elle va nous permettre de créer, d'entrainer et de tester notre réseau de neurones artificiels. 

### Keras 

API de réseau de neurones. Permettre d'ajouter une couche d'abstraction de haut niveau pour travailler plus facilement avec les réseaux de neurones.

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


# Prediction 

## Définition

### Classification problem

Sujet du machine learning relatif à faire apprendre à une machine le fait de regrouper 
des données selon un critère particulier. 

Dans notre exemple l'objectif va être de permettre à la machine de pouvoir prédir en 
fonction d'une image en input à quel "groupe" elle appartient, c'est à dire quel chiffre entre 0 et 9.

Notre classifier est donc un programme qui a pour but de distinguer les différentes images qui lui sont soumise et de les classer par chiffre.

Mais avant il est nécessaire de définir les caractéristiques mesurable qui nous permettent de distinguer les différents chiffres sur une image ? 

Dans notre classifier chaque image est représenté par un tableau de longueur n = 784, avec chaque valeur rerprésentant un pixel spécifique de l'image codé selon sa nuance de noir et blanc.

C'est donc la présence de tel pixel, à tel nuance (valeur numérique) et à tel endroit du tableau qui va nous permettre de pouvoir classer les images par chiffre. En effet, on va apprendre à la machine que par exemple que lorsqu'on a un 6 sur l'image alors dans la séquence on retrouve à tel index tel nuance de noir et blanc. 

Cependant il est difficile pour une machine de pouvoir travailler avec une matrice 28*28, on donc utiliser un algorithme qui va permettre d'extraire les portions les plus importantes d'une image pour obtenir des matrices 3*3 

### Concevoir le réseau de neurone 

L'idée ici serait de créer un réseaux de neurone capable de reconnaitre un chiffre sur une image. Il se ferait de la façon suivante: 

En entré on retrouve 784 neurones d'input qui reçoivent chaque pixel de l'image. 

En sortie j'ai 10 neurones d'ouput pour chaque chiffre. 

Si un neurone d'ouput est actif, alors le chiffre sur l'image correspond au chiffre associé à ce neurone d'output.

Notre objectif va être d'entrainer notre réseaux de neurones sur un dataset. A chaque image le réseaux de neurone va tester sa performance tout en sachant quel doit être l'output final. Si il parvient à sortir en output le bon chiffre alors il ne change rien. Si ce n'est pas le cas, alors il va devoir faire des ajustements dans la configuration de ces neurones. 

### Comment ajuster les neurones ? 

Les neurones artificiel sont des fonctions mathématiques qui prennent en entrée des inputs et donne en sortie un output. Dans une logique d'ajustement le neurone peut avoir besoin de modifier sa configuration interne. 

Pour modifier son output, le neurone artificiel peut: 

+ Augmenter ou diminuer son bias, c'est à dire la valeur limite à partir de laquelle il peut varier de 0 à 1
+ Augmenter ou diminuer le poids des inputs en entrée actifs, Plus un input à de poids et plus sa valeur va avoir de l'importance dans la valeur totale des inputs. 

On se poser la question: 

```
Itotal - b => plus proche de 1 ou de 0 ?
```


Chaque neurone qui composent un réseau doit faire en sorte d'avoir la bonne configuration optimale pour que l'output final correspondent à ce qui est attendu tel ou tel input du réseaux. Cette configuration optimale s'obtient via l'entrainement où le reseaux est soumis à un input et on lui donne l'output attendu. Il compare son ouput et celui attendu et peut détermer si il est proche ou non de la bonne configuration. Si ce n'est pas le cas il s'ajuste, et ainsi de suite...

### Couches de neurones 

Chaque neurone des couhes cachée => 1 decision boundary qui vient découpé le nuage de point pour séparé les décision binaire par exemple. 

Micro décision => micro choix intérmédiaire => vers un plus gros choix => Split le problèlme en micro problème binaire qu'un neurone peut résoudre en terme de probabilité binaire (entre 0 et 1) 


Chaque neurone est une fonction qui va calculer la probabilité entre 0 et 1 de correspondre aux caractéritiques qu'on lui demande de reconnaitre en fontion de tous les inputs qu'il reçoit en entrée, qui sont également des probabilité aux étapes précédentes.



Ex: En entrée j'ai 0,9 de probabilité d'avoir un cercle et 0,8 d'avoir un trait droit sur mon image => alors mon calcul dit que c'est à 0,9 de probabilité un "9".

=> Etape de logique supplémentaire 

Couche 1: Input => 784 valeurs numériques pour chaque nuance de gris de chaque pixel 

Couche 2: Probabilité que tel ou tel petite ligne soit reconnu sur l'image à partir des nuances de gris

Couche 3: Probabilité que tel ou tel patterne soit reconnu du l'image à partir des petits segments reconnu 

Couche 4: Probabilité que tel ou tel chiffre soit reconnu sur l'image à partir des pattern reconnus 

Backpropagation: a chaque fois que l'ouput final est pas bon, on applique cet algorithme sur le réseau et les neurones précédent sont update avec la nouvelle valeur... (résumé grossier) 

# Objectif 

Objectif de notre machine: ***Reconnaitre un chiffre entre 0 et 9 sur une image donnée***

## Dataset 

Le dataset d'entrainement est composé d'un ensemble de 60000 images. Chacune de ces images représentent un chiffre de 0 à 9, écrit à la main, centré sur une région de pixel au format 28*28.

| Data                           | Label                                                     |
|--------------------------------|-----------------------------------------------------------|
| Images représantant un chiffre | Le chiffre qui doit être prédit par le réseaux de neurone |

```Shape: (60000, 784)```

Pour tester la précision de notre ANN, nous avons également besoin de le tester sur un ensemble de donnée qu'il n'a pas déjà "vu". On appelle cet ensemble le ```dataset de test```.

TODO: https://scikit-learn.org/stable/modules/neural_networks_supervised.html + MNSIT

## ANN

Nous allons concevoir, entrainer et tester notre dataset

### Création du model

Classe qui nous permet de crée de nouvelle instance de model d'ANN

```
from keras.models import Sequential
```

Classe qui nous permet de crée de nouvelle instance de couche pour notre réseau de neurone

```
from keras.layers import Dense # Dense layers are "fully connected" layers
```

On crée notre réseau:

```
model = Sequential()
```

Dans notre réseau de neurone nous allons avoir un input pour chaque pixel de l'image. Ce qui fait que notre ANN va posséder 784 inputs.

 Notre réseau va posséder 10 neurones d'output, correspondant à chaque chiffre entre 0 et 9 reconnu sur l'image. 
 
```
# total chiffre entre 0 et 9
num_classes = 10

# On ajoute la couche des outputs, activé selon le chiffre reconnu sur l'image
model.add(Dense(units=num_classes, activation='softmax'))
```
Dans cette première version de notre réseau: 

+ Chaque neurone ```output``` possède un bias ```b``` qui peut être ajusté 
+ Chaque valeur d'input peut être ajusté par un poids ```weight``` tel que ```input * weight```
+ Chaque neurone ```output``` prends en entrée la valeur de chaque input ajusté par le poids, donc 784 donnée d'entrée
+ Il existe donc ```nb inputs * nb outputs + nb bias``` => ```784 * 10 + 10 = 7850``` valeurs qui peuvent être ajustées 

Nous allons ajoute une couche cachée (HL) à notre réseau tel que: 

+ Elle contient 32 noeuds (neurones)
+ Les neurones sont des fonctions sigmoid ( 0 < activation < 1 ) 
+ Les neurones prennent 784 entrée (chaque pixel de l'image)

```
# Le nombre de pixel qui composent chaque image
image_size = 784

# On une hidden layer à notre réseau, elle contient 32 noeuds (neurones), ils sont de type sigmoid ( 0 < activation < 1 ) et prennent 784 entrée (chaque pixel de l'image)
model.add(Dense(units=32, activation='sigmoid', input_shape=(image_size,)))
```

Il en resulte ```784 * 32 + 32 = 25120 + 32 * 10 + 10 = 25450``` valeurs ajustables.

On peut calculer ses valeurs grâce à une méthode de Keras:

```
# Total params: 25,450
model.sumary()
```
(Améliorer le model ? Retravailler les données d'entrées ou les paramètres du réseau (ex: cross validation))

### Entrainement et test du model 

```
model.compile(optimizer="sgd", loss='categorical_crossentropy', metrics=['accuracy'])

# On va entrainer le model sur le dataset
history = model.fit(x_train, y_train, batch_size=128, epochs=5, verbose=False, validation_split=.1)
# On va tester la performance de notre ANN
_ , accuracy  = model.evaluate(x_test, y_test, verbose=False)
print(accuracy)
```

Le réseau va être entrainé pendant 5 périodes (epoch), en modifiant les paramètres à chaques étape afin d'avoir les paramètres qui aboutissent à un plus petit taux d'erreur.

On va ensuite pouvoir évaluer la pérformance de notre model grâce à la méthode ```evaluate```. On obtient l'accuracy (précision) du model. 

Mon model obtient une précision de ```0.8912000060081482```.

# Questions 

## 1 - 

> Why use a separate dataset to measure the performance of an algorithm ?
What are the results you get when you test your algorithm on the same dataset used in training?

Pour tester la précision de notre ANN, nous avonss besoin de le tester sur un ensemble de donnée qu'il n'a pas déjà "vu". On appelle cet ensemble le ```dataset de test```. En effet lors de l'entrainement les paramètres de mon réseau de neurone ont été configurés de manière à ce que les prédictions de celui ci sur une image correspondent à celle du label qui lui est associé dans le dataset. Nous avons besoin d'évaluer la "fléxible" du réseau à travailler avec des images inconnues.

```J'obtient à peu de chose près la même précision autour de 90%```

## 2 - 

Le bias est la différence entre la prédiction moyenne d'un model et la valeur correcte qu'il essait de prédir. 

La variance est la variabilité des prédictions, c'est à dire la manière dont les prédictions sont "étalés" par le modèle.

La variance et le bias devraient avoir les plus petites valeur qu'il est possible. 

## 3 - 

 

