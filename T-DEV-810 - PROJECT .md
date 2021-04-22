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

### Radio de poumons infecté 

On va d'abord voir à quoi ressemble une image d'un poumon infecté: 

```
# Je récupère le chemin d'une image dans le cas d'un poumon infecté
pneumonia_x_ray = train_path + '/PNEUMONIA/' + os.listdir(train_path + '/PNEUMONIA')[0]
```

Je vais ensuite utiliser ma fonction ```imread()``` pour pouvoir lire l'image

```
imread(pneumonia_x_ray)
```

Notre image au format .jpeg est transformé en un tableau comme pour les images du MNSIT.

On peut ensuite vérifier la shape de notre tableau: 

```
imread(pneumonia_x_ray)
# (736, 1048)
```

On peut également visualiser l'image de la radio 

```
plt.imshow(imread(pneumonia_x_ray))
```

### Radio de poumons sains

Maintenant on va faire le même travaille de data-visualisation pour des poumons sains.

```
### On récupère la première image du dataset d'entrainement pour les poumons normaux (sains)
normal_x_ray = train_path + '/NORMAL/' + os.listdir(train_path + '/NORMAL')[0]
```

```
### On peut visualiser la radio pour les poumons non infectés par la pneumonie
plt.imshow(imread(normal_x_ray))
```

### Visualisation du format des images 

On va visualiser les dimensions de nos images dans le dataset d'entrainement pour connaitre si il existe ou non une trop grande disparité dans les dimensiosn des images (images dans des dimensions trop différentes). En effet notre CNN à besoin d'être entrainé sur des images dans des dimensions identiques. Les images réelles sont de fait dans des formats différents. 

```
# Chaque image est transformé en tableau de format d1*d2, e.g: pour la 1ère image de train => (736, 1048)
# Pour entrainer correctement notre CNN correctement, nous avons besoin de l'entrainer sur des images relativement de la
# même taille. Les dimensions d'images doivent donc être le moins disparâtre possible. 
# Pour se faire nous allons essayer de visualiser ces données.

# Dans un premier temps nous allons récupéré les dimensions pour chaque image d'un dataset (train) et les stocker
dim1 = []
dim2 = []
test = 'Hello World'

# On va ensuite itérer la liste des fichier (images) de notre dataset d'entainement (normaux) pour récupérer le chemin de chaque image
for x_ray_filename in os.listdir(train_path + '/NORMAL'):
    img = imread(train_path + '/NORMAL/' + x_ray_filename)
    d1,d2 = img.shape
    dim1.append(d1)
    dim2.append(d2)
```

On va ensuite utiliser un historigramme pour visualiser cette disparité dans les dimensions des images: 

```
sns.jointplot(dim1, dim2)
```

Voici le résultat: 

![histogramme des dimensions](./assets/histogramme-dimensions.png)

On va donc maitenant définir les dimensions avec laquelle nous allons donc redimensionner nos images:

```
np.mean(dim1)
# 1381.43
```

```
np.mean(dim2)
# 1667.73
```

Notre shape finale sera donc: 

```
image_shape = (1380, 1668)
```


## Traitement des données 

### Préparation des images et des méta données 

Nous avons 2 conditions dans notre études: 

+ Poumons infectés par la pneumonie 
+ Poumons sains 

Ce qui implique que notre dataset est strucutré par classe 

```
chest_Xray/
	test/
		PNEUMONIA/
		NORMAL/
	train/
		PNEUMONIA/
		NORMAL/
```

L'objectif va être de manipuler nos images pour ensuite pouvoir les donner à notre model. 

### Objectif 

Lorsqu'on utilise des CNN, on a besoin de beaucoup d'image, donc l'objectif serait à partir de notre dataset transformé les images pour obtenir plus de données. C'est ce qu'on appelle la ***data augmentation***.

L'autre objectif est la réduction de pixel présent dans une image, avec (1380, 1668) c'est plus de 2 000 000 de point. Pour fournir un réseau de neurone on a besoin de réduire la shape des images. C'est ce qu'on appelle l'***image normalization***


***data augmentation***: Augmenter le nombre d'image labelé pour nourir le réseau de neurone à partir d'un dataset de départ souvent peu fourni (on a besoin d'une 10 voir 100 de millier d'image pour entrainer correctemnt un ANN). Cependant il faut être prudent car cela peut mener à ce qu'on appelle du overfitting, c'est à dire que notre réseau devient trop spécifiquement entrainé pour notre dataset et obtient de mauvais résultat sur d'autre dataset de test ou cas réels.

### Image Normalization 

Lorsqu'on travaille avec des réseaux de neurone un des principaux objectifs dans le traitement des images est une mise à l'échelle. Ce qu'on entends par là c'est manipuler les données pour qu'elles obtiennent les mêmes dimensions.

De plus dans notre cas la dimension des images est beaucoup trop importante (1380, 1668) et notre mémoire va être à cour de mémoire pour faire tourner le model. 

Pour se faire je vais utiliser skimage qui contient des algorithmes qui vont me permettre de traité les image. En particulier c'est la fonction ```transform.resize()``` qui va nous être utile: 

```
# Redimensionner une image (normal)
from skimage import transform

# On défini la nouvelle shape de notre image
new_shape = (130, 130)

normal_x_ray_resize = transform.resize(imread(normal_x_ray), new_shape)

print(pneumonia_x_ray_resize.shape)
# (130, 130)

# On peut maintenant visualiser mon image redimensionnée 
plt.imshow(normal_x_ray_resize)
```

J'ai donc maintenant la solution pour mettre à l'échelle les images de mon dataset: 

```
# Je peux maitenant redimensionner mon dataset d'entrainement pour les poumons sains
train_data_normal_resized = []

# On défini la nouvelle shape de notre image
new_shape = (130, 130)

for x_ray_filename in os.listdir(train_path + '/NORMAL'):
    # image sous la forme d'un numpy array
    img = imread(train_path + '/NORMAL/' + x_ray_filename)
    # on redimmensionne avec img_resized en fonction de la shape voulue
    img_resized = transform.resize(img, new_shape)
    train_data_normal_resized.append(img_resized)
```

Cependant je peux vite me rendre compte que cette solution est très consommatrice en terme de ressource pour ma machine (~ 2-3 minutes) seulement pour les images de la classe "NORMAL" du dataset d'entrainement. Je vais donc tenter une nouvelle approche. 
 
#### Keras 

Keras fournis une classe ImageDataGenerator pour traiter les images en amont avant de les fournir au réseau de neurone.

```
# Meilleure solution
from keras_preprocessing.image import ImageDataGenerator

# Pour obtenir le chemin du dossier courrant
dirname = os.path.abspath('')

# /!\On a besoin de créer une instance de la classe ImageDataGenerator avant de pouvoir utiliser flow_from_directory()
core_idg = ImageDataGenerator()

# string qui représente le chemin vers le dossier qui contient notre dataset (ex: train dataset)
directory_path = os.path.join(dirname, 'chest_Xray/train') 

# On défini la nouvelle shape de notre image
new_shape = (130, 130)

# On va convertir nos images en greyscale pour obtenir 1 seul canal de couleur
color = 'grayscale'

# classes: On va laisser à None et utiliser les classes correspondant aux sous dossiers (NORMAL/PNEUMONIA)

# Ici on va selectionner binary car on est dans le cas où on a seulement deux catégories (NORMAL/PNEUMONIA)
class_mode = 'binary'

# Le dossier dans lequel on va sauvegarder nos images augmentées/normalisées
new_images_dir = os.path.abspath('') + '/chest_Xray_resized/train'
new_image_dir_prefix = 'resized'
subset = 'training'

print(new_images_dir)

train_gen = core_idg.flow_from_directory(
    directory=directory_path,
    target_size=new_shape,
    color_mode=color,
    classes=None,
    class_mode="binary",
    batch_size=32,
    shuffle=True,
    seed=None,
    save_to_dir=None,
    save_prefix="",
    save_format="png",
    follow_links=False,
    subset=None,
    interpolation="nearest",
)
```

Grâce à cette façon de faire, on peut générer l'image redimesionnéé et normaliée au moment de son utilisation. Cette méthode est moins consomatrice en ressource pour la machine. 

```
# On va maintenant visualiser
# Les labels de mon dataset
labels = os.listdir(train_path)

t_x, t_y = next(train_gen)
# La nouvelle shape des mes échantillons: (130, 130, 1)
print(t_x[0].shape)
plt.imshow(t_x[0])
```

On peut alors écrire une fonction qui va nous permettre de réutiliser la logique:

```
# Meilleure solution
from keras_preprocessing.image import ImageDataGenerator

# On peut créer une fonction pour réutiliser la logique pour chaque generator (test, train, ...)

def get_dataset_gen(dataset_name, new_shape):
    # /!\On a besoin de créer une instance de la classe ImageDataGenerator avant de pouvoir utiliser flow_from_directory()
    core_idg = ImageDataGenerator()
    
    # Pour obtenir le chemin du dossier courrant
    dirname = os.path.abspath('')

    # string qui représente le chemin vers le dossier qui contient notre dataset (ex: train dataset)
    directory_path = os.path.join(dirname, 'chest_Xray/' + dataset_name) 

    # On va convertir nos images en greyscale pour obtenir 1 seul canal de couleur
    color = 'grayscale'

    # classes: On va laisser à None et utiliser les classes correspondant aux sous dossiers (NORMAL/PNEUMONIA)

    # Ici on va selectionner binary car on est dans le cas où on a seulement deux catégories (NORMAL/PNEUMONIA)
    class_mode = 'binary'

    # Le dossier dans lequel on va sauvegarder nos images augmentées/normalisées
    new_images_dir = os.path.abspath('') + '/chest_Xray_resized/train'
    new_image_dir_prefix = 'resized'
    subset = 'training'
    
    
    
    dataset_gen = core_idg.flow_from_directory(
        directory=directory_path,
        target_size=new_shape,
        color_mode=class_mode,
        classes=None,
        class_mode="categorical",
        batch_size=32,
        shuffle=True,
        seed=None,
        save_to_dir=None,
        save_prefix="",
        save_format="png",
        follow_links=False,
        subset=None,
        interpolation="nearest",
    )
    return dataset_gen

train_gen = get_dataset_gen('train', (130, 130))
test_gen = get_dataset_gen('test', (130, 130))
```

### Batch Size 

C'est la quantité d'échantillon (provenant du dataset) avec lesquels l'ANN va être entrainé à la fois. Par défaut ```ImageDataGenerator.flow_from_directory()``` utilise un ```batch_size``` de 32. L'avantage d'un petit batch_size c'est les ressources de la machine allouer qui sont amoindrie. 

	

#### Binarisé les labels 








