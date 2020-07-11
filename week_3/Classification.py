# -*- coding: utf-8 -*-
"""ClassificationModelKeras.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11-m3A95CUvoQtlhW5kc7ysCMxrsg4BAX
"""

pandas dataframe: car_data
import keras
from keras.models import Sequential # linear stack of layers
from keras.layers import Dense


model = Sequential()
n_cols = car_data.shape[1]

model.add(Dense(5, activation= 'relu', input_shape=(n_cols,))) 
model.add(Dense(5, activation= 'relu'))
model.add(Dense(4, activation= 'softmax'))
# add method to add each dense layer
# specify number of neurons in each layer and activation function we would like to use
# relu is one of the recommended activation functions of hidden layers

model.compile(optimizer='adam', loss='categorical_crossentopy', metrics=['accuracy'])
model.fit(predictors, target, epochs=10)
# previous used gradient descent as the optimisation algorithm 
# and mean square error as our loss error as grand truth and predicted value
# gradient descent = adam benefit: do not need to specify the learning rate
predictions = model.predict(test_data)