import tensorflow as tf
from sklearn import cross_validation
from sklearn import datasets
from sklearn import metrics

learn = tf.contrib.learn

def my_model(features, target):
    target = tf.one_hot(target,3,1,0)
    print(target)

    logits, loss = learn.models.logistic_regression(features, target)

    train_op = tf.contrib.layers.optimize_loss(loss, tf.contrib.framework.get_global_step(), optimizer='Adagrad', learning_rate=0.1)
    return tf.arg_max(logits,1), loss, train_op

iris = datasets.load_iris()

x_train, x_test, y_train, y_test = cross_validation.train_test_split(iris.data, iris.target, test_size=0.2, random_state=0)

classifiier = learn.Estimator(model_fn=my_model)
classifiier.fit(x_train, y_train, steps=100)

y_predicted = classifiier.predict(x_test)

score = metrics.accuracy_score(y_test, y_predicted)
print('Accuracy: %.2f%%' % (score * 100))

