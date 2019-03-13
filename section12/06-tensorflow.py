# section12 / 06-tensorflow.py
# 노동시간에 따른 매출 예측 프로그램

# tensorflow 모듈 설치

import tensorflow as tf  # 오픈소스 라이브러리 모듈
hello = tf.constant('Hello World!')
sess = tf.Session()
print(sess.run(hello))
