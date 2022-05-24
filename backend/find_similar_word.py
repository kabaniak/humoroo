import gensim
# from gensim.models import Word2Vec

model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

def ten_similar(word1, word2):
    if word1 not in model or word2 not in model:
        print("one or both words not in dictionary")
        return -1
    
    simList = model.most_similar(positive=[word1, word2])

    for i in simList:
        word = i[0].replace("_", " ")
        print("When I think of "+word1+" my mind always wanders to "+word2+". I blame "+ word)
    return simList