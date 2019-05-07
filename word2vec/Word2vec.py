# coding=utf-8
import warnings

# 关闭报错
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

sentences = LineSentence('Output/stop_key_result.txt')

model = Word2Vec(sentences, hs=1, min_count=1, window=3, size=20)

# print model.wv.similarity(u'马', u'老师')
