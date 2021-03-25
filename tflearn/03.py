import tensorflow as tf

# 创建一个常量 op, 产生一个 1x2 矩阵. 这个 op 被作为一个节点
# 加到默认图中.
#
# 构造器的返回值代表该常量 op 的返回值.
# matrix1 = tf.constant([[3., 3.]])
# print("matrix1:",matrix1)
# # 创建另外一个常量 op, 产生一个 2x1 矩阵.
# matrix2 = tf.constant([[2.],[2.]])
# print("matrix2:",matrix2)
# 创建一个矩阵乘法 matmul op , 把 'matrix1' 和 'matrix2' 作为输入.
# 返回值 'product' 代表矩阵乘法的结果.
# product = tf.matmul(matrix1, matrix2)

# sess = tf.Session()

# result = sess.run(product)
# print("result:",result)

with tf.Session() as sess:
    matrix1 = tf.constant([[3., 3.]])
    print("matrix1:",matrix1)
    matrix2 = tf.constant([[2.],[2.]])
    print("matrix2:",matrix2)
    product = tf.matmul(matrix1, matrix2)
    with tf.device("/gpu:1"):
        result = sess.run(product)
        print("result:",result)
