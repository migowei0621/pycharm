import Tensorflow as tf


lstm_hidden_size = 12
num_steps = 10

lstm = tf.contrib.nn.BasicLSTMCell(lstm_hidden_size)
state = lstm.zero_state( tf.float32, batch_size=12)

loss = 0.0

for i in range(num_steps):
    if i >0:
        tf.get_veriable_scope().reuse_variables()

    lstm_output, state = lstm(current_input, state)
    final_output = tf.contrib.layers.fully_connected(lstm_output)
    loss += calc_loss(final_output,expected_output)