# coding=utf-8
from sklearn import datasets

iris = datasets.load_iris()

from sklearn.naive_bayes import GaussianNB

clf = GaussianNB()
clf = clf.fit(iris.data, iris.target)
y_pred = clf.predict(iris.data)

print("高斯朴素贝叶斯，样本总数： %d 错误样本数 : %d" % (iris.data.shape[0], (iris.target != y_pred).sum()))
