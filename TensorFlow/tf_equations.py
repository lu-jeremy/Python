import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


##x = tf.placeholder(tf.int32)
##
##a = tf.constant(1)
##b = tf.constant(2)
##c = tf.constant(10)
##
##quadratic_equation = tf.add(tf.add(tf.multiply(a, x**2), tf.multiply(b, x)), c)
##
##
##data = np.random.randint(100, size = 10)
##print(data)
##with tf.Session() as sess:
##    sess.run(tf.global_variables_initializer())
##    res = sess.run(quadratic_equation, feed_dict = {x : data})
##    print(res)
##
##plt.scatter(data, res)
##plt.show()

X_ONE = tf.placeholder(tf.int32)

X_TWO =  tf.placeholder(tf.int32)

M_ONE = tf.constant(1)

B_ONE = tf.constant(2)

M_TWO = tf.constant(-1)

B_TWO = tf.constant(5)

linear_equation_one = tf.add(tf.multiply(M_ONE, X_ONE), B_ONE)

linear_equation_two = tf.add(tf.multiply(M_TWO, X_TWO), B_TWO)

data_one = np.random.randint(100, size = 30)

data_two = np.random.randint(100, size = 20)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    
    res_one = sess.run(linear_equation_one, feed_dict = {X_ONE : data_one})
    
    res_two = sess.run(linear_equation_two, feed_dict = {X_TWO : data_two})



plt.scatter(data_one, res_one)
plt.plot(data_one, res_one)

plt.scatter(data_two, res_two)
plt.plot(data_two, res_two)
plt.show()
