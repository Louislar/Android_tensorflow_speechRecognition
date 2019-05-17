"""
tensorflow官方給的.pb轉.tflite的程式碼
https://www.tensorflow.org/lite/convert/python_api

"""

import tensorflow as tf

graph_def_file = "my_frozen_graph.pb"
input_arrays = ["wav_data"]
output_arrays = ["labels_softmax"]

converter = tf.lite.TFLiteConverter.from_frozen_graph(
  graph_def_file, input_arrays, output_arrays)
tflite_model = converter.convert()
open("converted_model.tflite", "wb").write(tflite_model)