import theano
import theano.tensor as T
import numpy as np
from theano import function
from random import random

# 定义变量

x = T.matrix('x')
w1 = theano.shared(np.array([random(), random()]))
w2 = theano.shared(np.array([random(), random()]))
w3 = theano.shared(np.array([random(), random()]))
b1 = theano.shared(1.)
b2 = theano.shared(1.)
learning_rate = 0.01

a1 = 1/(1 + T.exp(-T.dot(x,w1)-b1))
a2 = 1/(1 + T.exp(-T.dot(x,w2)-b1))

x2 = T.stack([a1,a2], axis=1)

a3 = 1/(1 + T.exp(-T.dot(x2,w3)-b2))


# 定义梯度和更新准则

a_hat = T.vector('a_hat') # Actual onput
cost = -(a_hat*T.log(a3)+(1-a_hat)*T.log(1-a3)).sum()

dw1,dw2,dw3,db1,db2 = T.grad(cost,[w1,w2,w3,b1,b2])

train = function(
    inputs = [x,a_hat],
    outputs = [a3,cost],
    updates = [
        [w1, w1-learning_rate*dw1],
        [w2, w2-learning_rate*dw2],
        [w3, w3-learning_rate*dw3],
        [b1, b1-learning_rate*db1],
        [b2, b2-learning_rate*db2]
    ]
)


# 训练模型

inputs = [[0,0],[0,1],[1,0],[1,1]]
outputs = [1,0,0,1]

# 遍历输入并计算输出
cost = []
for iter in range(30000):
    pred, cost_iter = train(inputs, outputs)
    cost.append(cost_iter)

print('The outputs of NN are:')

for i in range(len(inputs)):
    print('The output for x1=%d | x2=%d is %.2f' % (inputs[i][0],inputs[i][1],pred[i]))


import matplotlib.pyplot as plt
plt.plot(cost)
plt.show()





