import tensorflow as tf
from google.protobuf import text_format


# with tf.Session() as sess:
#     saver = tf.train.import_meta_graph('conv.ckpt-18000.meta')



def convert_pbtxt_to_pb(filename):
  """Returns a `tf.GraphDef` proto representing the data in the given pbtxt file.
  Args:
    filename: The name of a file containing a GraphDef pbtxt (text-formatted
      `tf.GraphDef` protocol buffer data).
  """
  with tf.gfile.FastGFile(filename, 'r') as f:
    graph_def = tf.GraphDef()
 
    file_content = f.read()
 
    # Merges the human-readable string in `file_content` into `graph_def`.
    text_format.Merge(file_content, graph_def)
    tf.train.write_graph( graph_def , './' , 'protobuf.pb' , as_text = False )
  return



convert_pbtxt_to_pb('conv.pbtxt')