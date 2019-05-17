"""
參考自: 
https://heartbeat.fritz.ai/deploying-pytorch-and-keras-models-to-android-with-tensorflow-mobile-a16a1fb83f2

"""
import os
import keras
from keras.datasets import mnist
from keras.layers import *
from keras.layers import Dense, ReLU, Softmax
from keras.optimizers import RMSprop
import numpy as np
import tensorflow as tf

"""
目標: 將train好的keras model轉換成tensorflow的.pb檔，並且讓他可以用tensorboard查看
        使用了網路上提供的keras_to_tensorflow()函數

結果: 成功讓keras的model轉換成tensorflow的.pb檔案
"""


def keras_to_tensorflow(keras_model, output_dir, model_name,out_prefix="output_", log_tensorboard=True):

    if os.path.exists(output_dir) == False:
        os.mkdir(output_dir)

    out_nodes = []

    for i in range(len(keras_model.outputs)):
        out_nodes.append(out_prefix + str(i + 1))
        tf.identity(keras_model.output[i], out_prefix + str(i + 1))

    sess = K.get_session()

    from tensorflow.python.framework import graph_util, graph_io

    init_graph = sess.graph.as_graph_def()

    main_graph = graph_util.convert_variables_to_constants(sess, init_graph, out_nodes)

    graph_io.write_graph(main_graph, output_dir, name=model_name, as_text=False)

    if log_tensorboard:
        from tensorflow.python.tools import import_pb_to_tensorboard

        import_pb_to_tensorboard.import_to_tensorboard(
            os.path.join(output_dir, model_name),
            output_dir)



model_stored = keras.models.load_model('minst_trained_model.h5')

#印出儲存的model內部狀態
model_stored.summary()

#創造儲存轉換後的model資料的資料夾，名稱為checkpoint
output_dir = os.path.join(os.getcwd(),"checkpoint")

#呼叫換函數
keras_to_tensorflow(model_stored, output_dir, model_name='minst_trained_model.pb')

