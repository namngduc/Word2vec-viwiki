from gensim.models.fasttext import FastText

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

    model_fasttext = FastText(size=150, window=10, min_count=2, workers=4, sg=1)
    model_fasttext.build_vocab(train_data)
    model_fasttext.train(train_data, total_examples=model_fasttext.corpus_count, epochs=model_fasttext.epochs)

    model_fasttext.wv.save("./model/fasttext_gensim.model")