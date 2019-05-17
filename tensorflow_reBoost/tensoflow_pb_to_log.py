"""
https://heartbeat.fritz.ai/deploying-pytorch-and-keras-models-to-android-with-tensorflow-mobile-a16a1fb83f2
讓pb檔案恢復成可以用tensorboard查看的狀態

已成功，這支程式是可以work的
"""

import tensorflow as tf

import os

model = 'my_frozen_graph.pb' #请将这里的pb文件路径改为自己的


from tensorflow.python.tools import import_pb_to_tensorboard
import_pb_to_tensorboard.import_to_tensorboard(
    os.path.join('', model),
    '')


# # graph = tf.get_default_graph()
# graph_def = tf.GraphDef()#graph.as_graph_def()
# graph_def.ParseFromString(tf.gfile.GFile(model, 'rb').read())
# tf.import_graph_def(graph_def, name='graph')
# summaryWriter = tf.summary.FileWriter('log/', graph_def)