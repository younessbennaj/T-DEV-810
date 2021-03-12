from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical
import numpy
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# X_train (input): Tableau qui forme l'échantillon d'image au format 28*28 qui représentent un chiffre de 0 à 9
# Chaque image est présenter par un tableau de 28 tableau qui contiennent 28 valeur numérique 
# Chaque valeur représente la nuance de gris d'un pixel

# Y_train (output): Tableau qui contient le chiffre qui a été reconnu à chaque image 
print(y_train)
# print(X_train[0][0])

# # On va récupérer les arguments donnés au programme
# args = arguments.get_args()

# # On va entrainer le réseau de neurone artificiel à partir du dataset.
# if args.mode == "train":

# # On va tester le réseau de neurone.
# elif args.mode == "test":

# # On va utiliser le réseau de neurone sur des nouvelles images de chiffre.
# elif args.mode == "use":