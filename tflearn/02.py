import tensorflow as tf


matrixl = tf.constant([[3., 3.]])

print(matrixl)

matrix2 = tf.constant([[2.],[2.]])

print(matrix2)

product = tf.matmul(matrixl, matrix2)

print (product)

with tf.Session() as sess:
    with tf.device("/cpu:0"):
        result = sess.run([product])
        print(result)