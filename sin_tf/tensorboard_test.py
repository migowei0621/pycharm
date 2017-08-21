import tensorflow as tf

input1 = tf.constant([1.0,2.0,3.0], name ="input1")
input2 = tf.Variable(tf.random_uniform([3]), name = "input2")
output = tf.add_n([input1,input2], name = "add")

sess = tf.Session()
sess.run(input2.initializer)
sess.run(output)

print(sess.run(output))
writer = tf.summary.FileWriter(".", tf.get_default_graph())
writer.close()