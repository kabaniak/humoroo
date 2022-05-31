def remove_plural(word1, word2, simList):
    result = []
    words_in_simList = []
    word_sim_dict = {}
    for word, sim in simList:
        words_in_simList.append(word)
        word_sim_dict[word] = sim

    for word, sim in simList:
        # true is this word is plural of another word in simList
        if word[:-1] in words_in_simList:
            words_in_simList.remove(word)
        elif word[:-1] + 'ies' in words_in_simList:
            words_in_simList.remove(word[:-1]+'ies')

    for w in words_in_simList:
        result.append([w, word_sim_dict[w]])


    return result

if __name__ == '__main__':
    word1, word2 = ['cats', 'dogs']
    simList = [['cat', 0.34], ['dog', 0.33], ['pig', 0.36], ['moon', 0.12], ['moons', 0.14]]
    print(remove_plural(word1, word2, simList))