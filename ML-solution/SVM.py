# encoding=utf-8

# 读取数据
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

sentences = LineSentence('C:\\workspace\\BulletAnalysis\\Corpus\\BosonNLP\\all.txt')

model = Word2Vec(sentences, min_count=1, size=20)

good_words = [line.strip().decode('utf-8') for line in
              open('C:\\workspace\\BulletAnalysis\\Corpus\\BosonNLP\\good.txt').readlines()]
bad_words = [line.strip().decode('utf-8') for line in
             open('C:\\workspace\\BulletAnalysis\\Corpus\\BosonNLP\\bad.txt').readlines()]

x_array = []
y_array = []

for item in good_words:
    x_array.append(model[item])
    y_array.append(1)

for item in bad_words:
    x_array.append(model[item])
    y_array.append(0)

# import warnings

# 关闭报错
# warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
# from gensim.models import Word2Vec

from sklearn import svm

clf = svm.SVC(kernel='poly')
clf = clf.fit(x_array, y_array)

# 分类结果测试
y_pred = clf.predict(x_array)
print("支持向量机，样本总数： %d 错误样本数 : %d" % (len(x_array), (y_array != y_pred).sum()))
