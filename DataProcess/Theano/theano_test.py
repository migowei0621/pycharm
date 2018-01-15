import theano.tensor as T
# import theano
# import numpy as np
# from theano import function

# lst = np.array([1,2,3,4,5,5,6,7,7,8])
# a = T.dscalar('a')
# b = T.dscalar('b')
# c = a * b
# f1 = function([a,b],c)
# lst = lst.reshape(2,5)
# print(lst)
# print(f1(1.5,3))



# # shared value

# from theano import shared
# x = T.iscalar('x')
# sh = shared(0)
# f2 = function([x],sh**2,updates=[(sh,sh+x)])
# print('function return value: %d' % f2(1))
# print('shared variable value: %d' % sh.get_value())
# print('function return value: %d' % f2(1))
# print('shared variable value: %d' % sh.get_value())


## calculate gradient  and sigmoid S(x) = 1/(1+ e^-x)

# from theano import pp # pretty-print
# x = T.fscalar('x')
# y1 = 1/(1 + T.exp(-x))
# y2 = T.sin(x)
# qy = T.grad(y2,x)
# f = function([x],y2)
# print(f(4))
# print(pp(qy))



# 梯度
import theano
import theano.tensor as T
from theano.ifelse import ifelse
import numpy as np
from random import random
from theano import function
# 定义变量:
x = T.matrix('x')
w = theano.shared(np.array([random(), random()]))
b = theano.shared(1.)
learning_rate = 0.01

#®定义数学表达式:
z = T.dot(x,w)+b
a = 1/(1+T.exp(-z))

a_hat = T.vector('a_hat') #Actual output
cost = -(a_hat*T.log(a) + (1-a_hat)*T.log(1-a)).sum()

dw,db = T.grad(cost,[w,b])

train = function(
    inputs = [x,a_hat],
    outputs = [a,cost],
    updates = [
        [w, w-learning_rate*dw],
        [b, b-learning_rate*db]
    ]
)

# 定义输入和权重
inputs = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
outputs = [0,0,0,1]

# 遍历所有输入并计算输出:
cost = []
for iteration in range(30000):
    pred, cost_iter = train(inputs, outputs)
    cost.append(cost_iter)

# 打印输出:
print('The outputs of the NN are:')
for i in range(len(inputs)):
    print('The output for x1=%d | x2=%d is %.2f' % (inputs[i][0],inputs[i][1],pred[i]))

# 绘制损失图:
print('\nThe flow of cost during model run is as following:')
import matplotlib.pyplot as plt
plt.plot(cost)
plt.show()


