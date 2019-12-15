# -*- coding: utf-8 -*-

from gensim.models import KeyedVectors
model = KeyedVectors.load('./model/word2vec_skipgram.model')

for word in model.most_similar("thành_phố"):
    print(word)