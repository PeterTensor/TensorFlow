import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

DATA_DAR = '/tmp/data'
NUM_STEPS = 1000
MINIBATCH_SIZE = 100

data = input_data.read_data_sets(DATA_DAR , one_hot = True)
#使用占位符placeholder和变量Varible
#784表示维度为28x28的像素展开为一个向量，None表示每次不指定使用的图片的数量
X = tf.placeholder(tf.float32,[None , 784])
W = tf.Varible(tf.zeros([784,10]))

y_true = tf.placeholder(tf.float32 , [None ,10])
y_pred = tf.matmul(X , W)
#cross_entropy表示模型中的交叉熵，损失函数
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = y_pred , label = y_true))
#学习率为0.5，用控制梯度下降优化器改变权重的速度
gd_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

correct_mask = tf.equal(tf.argmax(y_pred , 1) , tf.argmax(y_true , 1))
accuracy = tf.reduce_mean(tf.cast(correct_mask , tf.float32))

with tf.Session() as sess:
    #Train
    sess.run(tf.global_variables_initializer())
    for _ in range(NUM_STEPS):
        batch_xs , batch_ys = data.train.next_batch(MINIBATCH_SIZE)
        sess.run(gd_step , feed_dict = {x: batch_xs , y_true: batch_ys})
    #test
    ans = sess.run(accuracy , feed_dict = {x:data.test.images , y_true:data.test.label})
    
print('Accuracy:{:.4}%'.format(ans*100))
