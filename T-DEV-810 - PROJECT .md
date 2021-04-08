# T-DEV-810 - PROJECT 

## Objectif 

Nous avons traité jusqu'à présent des ensembles d'images préalablement condirionnés (voir bootstrap et le dataset MNIST). 

Nous allons maintenant traité le cas relatif au travail avec des fichiers d'images réelles au format .jpeg

Notre objectif va être de réaliser un model (CNN) capable de prédir à partir d'une image (radio des poumons), si le patient est infecté par la bactérie de la pneumonie ou non.

## Notebook 

### Création du notebook

On va créer notre jupyter notebook

On va d'abord récupérer nos datasets ```test``` et ```train```

```
import os

# On récupère le dossier qui contient nos datasets
data_dir = 'chest_Xray'

os.listdir(data_dir)
# [‘.DS_Store', 'test', 'train', 'val']
```

## Datasets

On va d'abord installer les différentes dépendences dont on va avoir besoin: 

```
# On importe nos différentes dépendences
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
```

On va récupérer la methode de matplotlib qui nous permet de lire les images: 

```
# Va nous permettre de lire directement un fichier image
from matplotlib.image import imread
```

On va récupérer le chemin de chaque dataset:

```
# On récupère le chemin pour les data de test
test_path = data_dir + '/test'

# Puis le chemin pour les data d'entrainement
train_path = data_dir + '/test'
```

On va ensuite lister les deux types de dataset qu'on retrouve dans celui de test: 

```
os.listdir(train_path)
```

On se retrouve donc avec les images qui représentent une radio avec des poumons normaux (non infectés) et des poumons infectés par la pneumonie (bactérie)

## Datavisualization

On va d'abord voir à quoi ressemble une image d'un poumon infecté: 

```
# Je récupère le chemin d'une image dans le cas d'un poumon infecté
pneumonia_cell = train_path + '/PNEUMONIA/' + os.listdir(train_path + '/PNEUMONIA')[0]
```

Je vais ensuite utiliser ma fonction ```imread()``` pour pouvoir lire l'image

```
imread(pneumonia_cell)
```

Notre image au format .jpeg est transformé en un tableau comme pour les images du MNSIT.

On peut ensuite vérifier la shape de notre tableau: 

```
imread(pneumonia_cell)
# (736, 1048)
```








