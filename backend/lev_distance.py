from Levenshtein import distance as lev

def rank_by_lev_dist(word1, word2, simList):

    word_lev_dict = {}
    word_sim_dict = {}
    for word, sim in simList:
        lev_to_word1 = lev(word, word1)
        lev_to_word2 = lev(word, word2)
        lev_sum = lev_to_word1 + lev_to_word2
        word_lev_dict[word] = lev_sum
        word_sim_dict[word] = sim

    dict_sorted = dict(sorted(word_lev_dict.items(), key = lambda x:x[1]))
    lev_simList = list(dict_sorted.keys())

    #print('Most lev-similar words for {} and {}'.format(word1, word2))
    #print(lev_simList)
    ranked_list = []
    for w in lev_simList:
        word_sim = [w, word_sim_dict[w]]
        ranked_list.append(word_sim)

    return ranked_list

if __name__ == '__main__':
    word1, word2 = ['cats', 'dogs']
    simList = [['cat', 0.34], ['dog', 0.33], ['pig', 0.36], ['moon', 0.12]]
    rank_by_lev_dist(word1, word2, simList)