import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import mnist_inference

INPUT_NODE = 784
OUTPUT_NODE = 10
LAYER1_NODE = 500

def train(mnist):
    with tf.name_scope('input'):
        x = tf.placeholder(tf.float32,[None,mnist_inference.INPUT_NODE])