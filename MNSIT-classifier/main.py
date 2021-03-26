# On importe notre dataset
from tensorflow.keras.datasets import mnist
# Lib pour la visualisation de données
from matplotlib import pyplot as plt
# Lib pour travailler avec les tableaux
import numpy as np

from tensorflow import keras

# Classe pour créer les couches du réseau
from tensorflow.keras.layers import Dense
# Classe pour créer une nouvelle instance de réseau
from tensorflow.keras.models import Sequential

class Classifier:
    def __init__(self):
        self.image_size = 28

        # On va séparer nore dataset en distinguant l'échantillon d'entrainement et l'échantillon de test
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        # X_train (input): Tableau qui forme l'échantillon d'image au format 28*28 qui représentent un chiffre de 0 à 9
        # Chaque image est présenter par un tableau de 28 tableau qui contiennent 28 valeur numérique 
        # Chaque valeur représente la nuance de gris d'un pixel

        # Y_train (output): Tableau qui contient le chiffre qui a été reconnu à chaque image 

        self.train_data = x_train, y_train
        self.test_data = x_test, y_test
    # Methode de notre classe pour afficher les statistiques de répartition des chiffres dans le dataset d'entrainement 
    def display_statistics(self):
        columns = ['digits', 'train', 'test']
        rows = list(map(str, range(0, 10)))
        print(rows)
        print(columns)

        # On récupère la distribution de chaque chiffre dans le dataset d'entrainement
        _, y_train = self.train_data
        counts_train = np.bincount(y_train)

        # On récupère la distribution de chaque chiffre dans le dataset de test
        _, y_test = self.test_data
        counts_test = np.bincount(y_test)


        # Pour afficher l'histogramme
        # fig, ax = plt.subplots()
        # ax.bar(range(10), counts, width=0.8, align='center')
        # ax.set(xticks=range(10), xlim=[-1, 10])

        # Mise en forme du tableau
        n_rows = len(rows)
        cell_text = []

        # On crée les lignes de notre tableau
        for i in range(n_rows):
            print(rows[i])
            cell_text.append([rows[i], counts_train[i], counts_test[i]])

        
        # On supprime les éléments grapgique du graph
        ax = plt.gca()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # On supprime le cadre du graph
        plt.box(on=None)

        # On ajoute un peu de style à notre tableau
        colors = plt.cm.BuPu(np.full(len(columns), 0.1))

        # On crée notre tableau et on le centre
        table = plt.table(
            cellText=cell_text,
            colColours=colors,
            colLabels=columns, 
            loc='center')

        # On agrandi les valeur du tableau
        table.scale(1, 1.5)

        plt.show()


    # Methode de notre classe pour afficher via matplotlib la première image de l'échantillon d'entrainement
    # dataset: le dataset d'entraintement ou de test
    # index: l'index de l'image qu'on souhaite afficher
    def display_image(self, dataset, index):
        if dataset == 'train':
            x_train, _ = self.train_data
            data = x_train
        else:
            x_test, _ = self.test_data
            data = x_test

        image = data[index]
        pixels = image.reshape((28, 28))
        plt.imshow(pixels, cmap='gray')
        plt.show()

    def reshape_dataset(self, dataset):
        num_classes = 10
        if dataset == 'train':
            x_train, y_train = self.train_data
            data = x_train
            y = keras.utils.to_categorical(y_train, num_classes)
        else:
            x_test, y_test = self.test_data
            data = x_test
            y = keras.utils.to_categorical(y_test, num_classes)


        arr = np.array(data)
        # from shape [n, 28*28]
        arr = arr.transpose(1,2,0)
        arr = arr.reshape(-1, arr.shape[-1])
        arr = arr.transpose(1,0)
        # to shape [n, 784]

        return arr, y

    # Ajouter la méthode load_model
    def load_model(self):

        # Chaque image est composé de 28*28=784 pixels de nuances de gris
        # C'est le nombre d'inputs de notre réseau de neurone
        image_size = 784

        # Lorsqu'une machine résoud un problème de classification, elle catégorise par classe;
        # Dans notre cas ce sont les chiffres de 0 à 9, soit 10 classes
        num_classes = 10

        # On va crée notre réseau de neurone à partir de la classe Sequential
        # Cela nous retourne une nouvelle instance d'ANN
        model = Sequential()

        # On va ajouter une couche cachée (HL) à notre réseau
        # On va ajouter 32 noeuds (neurones), qui sont des fonctions sigmoid (0 < activation < 1)
        # Chaque neurone prend 784 en entrée (nombre d'input)
        model.add(Dense(units=32, activation='sigmoid', input_shape=(image_size,)))

        # On va ensuite ajouter la couche de neurone d'output
        # Selon leur activation, on va pouvoir connaitre quel chiffre à été reconnu sur l'image 
        model.add(Dense(units=num_classes, activation='softmax'))

        # On peut calculer le nombres de valeurs ajustables et l'afficher dans la console
        model.summary()

        #return model
        return model

    # Ajouter la methode train_model
    def train_model(self, model, train, test):
        # x => La donnée en entrée, chiffre de 0 à 9 centré sur une region de pixel au format 28*28
        # y => Le label, c'est à dire le chiffre qui doit être prédit par le réseau de neurone
        x_train, y_train = train
        x_test, y_test = test

        model.compile(optimizer="sgd", loss='categorical_crossentropy', metrics=['accuracy'])
        # On va entrainer le model sur le dataset
        history = model.fit(x_train, y_train, batch_size=128, epochs=5, verbose=False, validation_split=.1)
        # On va tester la performance de notre ANN
        _ , accuracy  = model.evaluate(x_test, y_test, verbose=False)
        print(accuracy)
        # On va visualiser le résultat
        plt.plot(history.history['accuracy'])
        plt.plot(history.history['val_accuracy'])
        plt.title('model accuracy')
        plt.ylabel('accuracy')
        plt.xlabel('epoch')
        plt.legend(['training', 'validation'], loc='best')
        plt.show()

        # train model on training set

    # Ajouter la méthode test_model

# On crée une nouvelle instance de notre class
c = Classifier()

# # On affiche la 4 ème image du dataset d'entraintement
# c.display_image('train', 4)

# # On affiche la distribution de chaque chiffre par dataset
# c.display_statistics()

# On récupère le dataset d'entrainenement et de test
train = c.reshape_dataset('train')
test = c.reshape_dataset('test')

model = c.load_model()

# On va entrainer notre model avec les datasets d'entraintement et de test
c.train_model(model, train, test)