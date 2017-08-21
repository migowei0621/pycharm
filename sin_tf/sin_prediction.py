import tensorflow as tf
import numpy as np

import matplotlib as mpl
mpl.use('Agg') #?
from matplotlib import pyplot as plt

learn = tf.contrib.learn

HIDDEN_SIZE = 30
NUM_LAYERS = 2
TIMESTEPS = 10
TRAINING_STEPS = 10000
BATCH_SIZE = 32

TRAINING_EXAMPLES = 10000
TESTING_EXAMPLES = 1000
SAMPLE_GAP = 0.01

def generate_data(seq):
    X =[]
    y =[]
    for i in range(len(seq) - TIMESTEPS - 1):
        X.append([seq[i: i + TIMESTEPS]])
        y.append([seq[i + TIMESTEPS]])
    return np.array(X, dtype=np.float32), np.array(y, dtype=np.float32)

def lstm_model(X, y):

    # r1.0后 tf.nn.rnn_cell 改为tf.contrib.rnn
    lstm_cell = tf.contrib.rnn.BasicLSTMCell(HIDDEN_SIZE)
    cell = tf.contrib.rnn.MultiRNNCell([lstm_cell] * NUM_LAYERS)

    # r1.0后tf.unpack() 改为 tf.unstack()
    x_ = tf.unstack(X, axis = 1)
    print(x_)
    # r1.0后tf.nn.rnn() 改为 tf.contrib.rnn.static_rnn()
    output, _ = tf.contrib.rnn.static_rnn(cell, x_, dtype=tf.float32)
    output = output[-1]

    prediction, loss = learn.models.linear_regression(output, y)

    train_op = tf.contrib.layers.optimize_loss(loss, tf.contrib.framework.get_global_step(), optimizer="Adagrad", learning_rate=0.1)
    return prediction, loss, train_op

regressor = learn.Estimator(model_fn = lstm_model)

test_start = TRAINING_EXAMPLES * SAMPLE_GAP
test_end = (TRAINING_EXAMPLES + TESTING_EXAMPLES) * SAMPLE_GAP
train_X, train_y= generate_data(np.sin(np.linspace(0,test_start,TRAINING_EXAMPLES, dtype=np.float32)))
test_X, test_y = generate_data(np.sin(np.linspace(test_start,test_end,TESTING_EXAMPLES, dtype = np.float32)))

regressor.fit(train_X, train_y, batch_size=BATCH_SIZE, steps = TRAINING_STEPS)
predicted = [[pred] for pred in regressor.predict(test_X)]
rmse = np.sqrt(((predicted - test_y) ** 2).mean(axis=0))
print("Mean Square Error is: %f" % rmse[0])


