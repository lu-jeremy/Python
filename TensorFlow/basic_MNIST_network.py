import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import matplotlib.pyplot as plt


# Read data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

image_size = 28
labels_size = 10
learning_rate = 0.05
steps_number = 1000
batch_size = 100

training_data = tf.placeholder(tf.float32, [None, image_size*image_size])
labels = tf.placeholder(tf.float32, [None, labels_size])

W = tf.Variable(tf.truncated_normal([image_size*image_size, labels_size], stddev=0.1))
b = tf.Variable(tf.constant(0.1, shape=[labels_size]))

output = tf.matmul(training_data, W) + b

loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=labels, logits=output))

train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss)
correct_prediction = tf.equal(tf.argmax(output, 1), tf.argmax(labels, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

sess = tf.InteractiveSession()
sess.run(tf.global_variables_initializer())

for i in range(steps_number):
  input_batch, labels_batch = mnist.train.next_batch(batch_size)
  feed_dict = {training_data: input_batch, labels: labels_batch}

  train_step.run(feed_dict=feed_dict)

  if i%100 == 0:
    train_accuracy = accuracy.eval(feed_dict=feed_dict)
    print("Step %d, training batch accuracy %g %%"%(i, train_accuracy*100))
    

test_accuracy = accuracy.eval(feed_dict={training_data: mnist.test.images, labels: mnist.test.labels})

fig = plt.figure(figsize = (8, 8))


for i in range(1, 21):

    fig.add_subplot(5, 4, i)
    
    second_arr = mnist.train.images[i]
    second_arr = second_arr.reshape([28, 28])

##    plt.title("Training Labels {0}".format(list(mnit.train.labels[i]).index(1)))
    plt.imshow(second_arr)
plt.title("Training Images")
plt.show()

fig = plt.figure(figsize = (8, 8))
for i in range(1, 21):

    fig.add_subplot(5, 4, i)

    first_arr = mnist.test.images[i]
    first_arr = first_arr.reshape([28, 28])
##    plt.title("Test Labels {0}".format(list(mnist.test.labels[i]).index(1))) 
    plt.imshow(first_arr)
plt.title("Test Images")

plt.show()


print("Test accuracy: %g %%"%(test_accuracy*100))
