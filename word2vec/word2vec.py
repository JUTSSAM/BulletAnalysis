# coding=utf-8
import warnings

warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')

import gensim

sentences = gensim.models.word2vec.LineSentence('Participle/output.txt')
model = gensim.models.word2vec.Word2Vec(sentences, hs=1, min_count=1, window=3, size=20)
print model
