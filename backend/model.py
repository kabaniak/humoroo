from gensim.models import KeyedVectors
import time
import random
import WordsToComic as WordsToComic
from textblob import TextBlob
from remove_plural import remove_plural
from lev_distance import rank_by_lev_dist
from remove_duplicate import remove_duplicate

startTime = time.perf_counter()
model = KeyedVectors.load_word2vec_format("./GoogleNews-vectors-negative300.bin", binary=True)
endTime = time.perf_counter()
print("Modelling took " + str(endTime-startTime) + " seconds")

#Takes words as input, returns full joke as list of 3 strings
def pass_joke(word1, word2):
    # startTime = time.perf_counter()
    # #load model
    # model = KeyedVectors.load_word2vec_format("./humoroo/src/GoogleNews-vectors-negative300.bin", binary=True)
    # endTime = time.perf_counter()
    # print("Modelling took " + str(endTime-startTime) + " seconds")

    startTime = time.perf_counter()
    #find 10 similar words

    #added code:
    simList = model.most_similar(positive=[word1, word2])
    simList = remove_plural(word1, word2, simList)
    simList = remove_duplicate(word1, word2, simList)
    simList = rank_by_lev_dist(word1, word2, simList)
    word3 = simList[0][0].replace("_", " ")
    #end of added code

    #original code:
    #word3 = model.most_similar(positive=[word1, word2])[0][0].replace("_", " ")
    endTime = time.perf_counter()
    print("Joke-writing " + str(endTime-startTime) + " seconds")

    joke = ["When I think of {}...".format(word1), "...my mind always wanders to {}.".format(word2), "I blame {}.".format(word3)]
    print(joke)
    WordsToComic.GenerateComic(word1, word2, word3, joke[0], joke[1], joke[2])
    return joke

#Running tests
def create_joke(word1, word2):
    string = ["{}", "{}", "{}"]
    if word1 not in model or word2 not in model:
        print("one or both words not in dictionary")
        return -1
    
    format = random.randint(0,7)
    word = random.randint(0,9)

    #added code:
    simList = model.most_similar(positive=[word1, word2])
    simList = remove_plural(word1, word2, simList)
    simList = remove_duplicate(word1, word2, simList)
    simList = rank_by_lev_dist(word1, word2, simList)
    wordToUse = simList[word]
    # end of added code

    #Original code:
    #wordToUse = model.most_similar(positive=[word1, word2])[word]


    def pos_finder(text):
        if len(text.split()) > 1:
            return "noun"
        blob = TextBlob(word)
        pos = blob.tags[1]
        if pos.startswith("JJ"):
            return "adj"
        elif pos.startswith("NN"):
            return "noun"
        elif pos.startswith("VB"):
            return "verb"
        
    word1pos = pos_finder(word1)
    word2pos = pos_finder(word2)

    #changed code:
    wordToUsepos = pos_finder(wordToUse[0])

    #original code:
    #wordToUsepos = pos_finder(wordToUse)

    if format == 0:
            string= ["{}", "{}", "{}"]
    elif format == 1:
            string = ["When I think of {}", "my mind always wanders to {}.", "I blame {}"]
    elif format == 2:
            string = ["I like my {}", "like I like my {}.", "Surrounded by {}."]
    elif format == 3:
            string = ["You have {}.", "I have {}.", "Baby, let's get together and make {}!"]
    elif format == 4:
            string = ["I have a {}.", "I have a {}.", "UNGH! {}!"]
    elif format == 5:
            string = ["What started as addiction to {}", "and {}", "landed me in rehab for {} withdrawal."]
    elif format == 6:
            string = ["I like {}", "and you like {}.", "Wanna start a {} club?"]
    elif format == 7:
            string = ["I have a {}.", "I have a {}.", "UNGH! {}!"]
        
    formWord = wordToUse[0].replace("_", " ")
    return string, formWord

# print(model.most_similar(positive=["Obama", "zombies"]))
#pass_joke("mountain", "nature")
#Testing
# while(1):
#     input1 = input("Word 1: ").strip().replace(" ", "_")
#     input2 = input("Word 2: ").strip().replace(" ", "_")
#     #input3 = input("Format? (1-6)")

#     startTime = time.perf_counter()
#     # ten_similar_format(input1,input2,input3)
#     pass_joke(input1,input2)
#     endTime = time.perf_counter()
#     print("Joke writing took " + str(endTime-startTime) + " seconds")