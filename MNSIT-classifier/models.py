from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Flatten, Dense, Activation

import utils

def deepnet():
    model = Sequential()

    model.add(Flatten(input_shape=utils.IMG_SHAPE))

    model.add(Dense(utils.NUM_CLASSES))
    model.add(Activation("softmax"))

    return model