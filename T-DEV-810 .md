# T-DEV-810 

## Objectif 

Mettre en place ***un réseau de neurone artificiel*** capable de reconnaitre un ***chiffre*** (integer) compris entre ***0 et 9***.

### Intelligence aritficielle 

Programme qui a pour but d'imiter les fonctions cognitives humaines. Comme l'intelligence naturelle (ex: humaine), elle est basé sur la fléxibilité, c'est à dire la capacité de l'intelligence à apprendre des ses experiences.

### Neurone artificiel 

Entité logique (porte logique) basé sur deux principes fondamentaux: 

+ Un neurone artificiel suit des règles logiques, qui lui sont propres, de façon à donner un certain output à partir des certains inputs. 
+ Un neurone artificiel peut à partir des mêmes inputs, mener à un output différent si on change son configuration interne.

### Un réseau de neurone artificiel

Approche visant à créer une intelligence artificielle. Cette approche est est basé sur la mise en relation de neurones artificiels sous forme de couche lié les unes aux autres. L'output des neurones situé dans les couches inférieures sont l'input des neuronnes des couches supérieurs. 

### Image recognition 

Programme visant à faire reconnaitre, par une machine, une information visuelle à partir d'une image donnée. La compléxité tiens à la fois dans les différences entre les fondements de la vision humaine et de celle des machines, mais également dans le manque de flexibilité d'une approche algoritmique classique pour résoudre ce problème. C'est pour cela qu'on utilise une approche utilisant les intelligence aritificielle, flexible par nature. 

## Dataset

Le dataset est composé de 60000 images représentant un chiffre compris entre 0 et 9. Ces images sont composé d'une grille de 28*28 pixel. Chacun de ces pixels représentes une nuances de gris. La nuance la plus forte indique l'objet à étudier. 

Les pixels sont réprésenté par la machine sous la forme d'une valeur numérique, représentant la nuance de gris corresponsante à ce pixel. L'image pour la machine est donc représenté sous la forme d'un ensemble de valeur numérique.s

La coordonnées [10,12,14] représente le pixel de la ligne 12, à la colonne 14, de la 10ème image. 

### Objectif et rôle 

Dans le cas d'une intelligence artificielle de reconnaissance d'images, l'objectif d'un dataset est d'entrainer un réseau de neurone à reconnaitre une information visuelle.


