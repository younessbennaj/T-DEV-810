from tensorflow.keras.datasets import mnist
from matplotlib import pyplot as plt
import numpy as np

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
        ccolors = plt.cm.BuPu(np.full(len(columns), 0.1))

        # On crée notre tableau et on le centre
        table = plt.table(
            cellText=cell_text,
            colColours=ccolors,
            colLabels=columns, 
            loc='center')

        # On agrandi les valeur du tableau
        table.scale(1, 1.5)

        plt.show()


    # Methode de notre classe pour afficher via matplotlib la première image de l'échantillon d'entrainement
    # dataset: le dataset d'entraintement ou de test
    # index: l'index de l'image qu'on souhaite afficher
    def display_image(self, dataset, index):
        train = 'train'
 
        if dataset == 'train':
            x_train, _ = self.train_data
            data = x_train
        else:
            x_test, _ = self.train_test
            data = x_test

        image = data[index]
        pixels = image.reshape((28, 28))
        plt.imshow(pixels, cmap='gray')
        plt.show()

c = Classifier()

# On affiche la 4 ème image du dataset d'entraintement
c.display_image('train', 4)

# On affiche la distribution de chaque chiffre par dataset
c.display_statistics()