import tensorflow as tf
#tensorflow的版本号
print(tf.__version__)
h = tf.constant(1,shape = None)
w = tf.constant(2,shape = None)
hw = h + w
with tf.Session() as sess:
    ans = sess.run(hw)
print(ans)
print(h)
print(w)
