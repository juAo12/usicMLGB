from tensorflow.python.keras import backend as K
import tensorflow as tf
import numpy as np


def auc(y_true, y_pred):
    # 由于 tf.metrics.auc 自身的问题，导致 AUC 虚高
    tf_auc = tf.metrics.auc(y_true, y_pred, num_thresholds=5000)[1]
    K.get_session().run(tf.local_variables_initializer())
    return tf_auc


def fast_auc(y_true, y_prob):
    """
    auc 快速算法：让模型给一堆样本（正负标签已知）打分，然后将这堆样本打分从大到小排序，正样本能够正确地排在负样本前面的概率

    正样本排在负样本前面的概率 =  sum(正样本排在负样本前面的情况) / 所有正样本和负样本的排序情况

    如以下模型打分从高到低的排序结果：1 0 1 1 0 0

    例子：
    y_true = [1, 1, 1, 0, 0, 0]
    y_prob = [0.8, 0.6, 0.5, 0.7, 0.4, 0.3]
    auc = 0.778

    :param y_true:
    :param y_prob:
    :return:
    """
    y_true = np.asarray(y_true)  # type: np.ndarray
    indices = np.argsort(y_prob)    # 倒序，从预测值低开始遍历，方便统计正样本排在负样本前面的情况
    y_true = y_true[indices]
    print(y_true)
    nfalse = 0  # 负例数
    auc = 0.0
    n = len(y_true)
    for i in range(n):
        y_i = y_true[i]
        nfalse += (1 - y_i)
        auc += y_i * nfalse
    if (nfalse * (n - nfalse)) == 0:
        return -1
    return float(auc) / (nfalse * (n - nfalse))

if __name__ == '__main__':
    y_true = [1, 1, 1, 0, 0, 0]
    y_prob = [0.8, 0.6, 0.5, 0.7, 0.4, 0.3]
    auc = fast_auc(y_true, y_prob)
    print(auc)