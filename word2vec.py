from gensim.models import Word2Vec

# path data
pathdata = './datatrain.txt'

def read_data(path):
    traindata = []
    sents = open(path, 'r', encoding='utf-8').readlines()
    for sent in sents:
        traindata.append(sent.split())
    return traindata


if __name__ == '__main__':
    train_data = read_data(pathdata)

    model = Word2Vec(train_data, size=150, window=10, min_count=2, workers=4, sg=0)
    model.wv.save("./model/word2vec_skipgram.model")