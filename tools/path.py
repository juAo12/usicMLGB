import logging
import tensorflow as tf

# 创建一个张量
tensor = tf.constant([[1, 2], [3, 4]])

# 计算所有元素的总和
total_sum = tf.reduce_sum(tensor, name='total')

# 沿着第一个轴（行）求和
row_sum = tf.reduce_sum(tensor, axis=0, name='row')

# 沿着第二个轴（列）求和
col_sum = tf.reduce_sum(tensor, axis=1, name='col')

print(total_sum, row_sum, col_sum)
logging.error(f'total_sum : {total_sum}')
logging.error(f'row_sum : {row_sum}')
logging.error(f'col_sum : {col_sum}')
