import keras
from keras.datasets import mnist
from keras.layers import Dense, ReLU, Softmax
from keras.optimizers import RMSprop
import numpy as np
import tensorflow as tf

"""
目標: 辨識手寫數字0~9
DNN input: 28*28的手寫數字圖像
DNN output: 預測結果為0-9的one hot encodeing
"""


#label種類
NUM_CLASSES = 10

#下載資料集
(x_train, y_train), (x_test, y_test) = mnist.load_data()

#將圖片reshape成一長條vector
x_train = x_train.reshape(x_train.shape[0], 28*28)
x_test = x_test.reshape(x_test.shape[0], 28*28)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

print(x_train.shape)

#label轉乘one hot encoding
y_train = keras.utils.to_categorical(y_train, NUM_CLASSES)
y_test = keras.utils.to_categorical(y_test, NUM_CLASSES)

#建造model
model = keras.Sequential()
model.add(Dense(30, activation = 'relu', input_shape = (784, )))
model.add(Dense(20, activation = 'relu'))
model.add(Dense(10, activation = 'softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer=RMSprop(),
              metrics=['accuracy'])

batch_size = 128
num_classes = 10
epochs = 10
history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=1,
                    validation_data=(x_test, y_test))


#把檔案儲存成h5py格式，才會方便之後轉成.tflite檔案
save_file_name = 'minst_trained_model.h5'
model.save(save_file_name)

# Convert to TensorFlow Lite model.
converter = tf.lite.TFLiteConverter.from_keras_model_file(save_file_name)
tflite_model = converter.convert()
open("mnist_trained_model.tflite", "wb").write(tflite_model)


