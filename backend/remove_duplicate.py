# take two words, and a list of similar words, return a list with no duplicates
def remove_duplicate(word1, word2, simList):
    result = []

    for word, sim in simList:
        if word == word1 or word == word2:
            continue
        elif word in word1 or word in word2:
            continue
        elif word1 in word or word2 in word:
            continue
        else:
            result.append([word, sim])
    return result

if __name__ == '__main__':
    word1, word2 = ['cats', 'dogs']
    simList = [['cat', 0.34], ['dog', 0.33], ['pig', 0.36], ['moon', 0.12], ['moons', 0.14]]
    print(remove_duplicate(word1, word2, simList))