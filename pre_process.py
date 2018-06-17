import pandas as pd
import numpy as np
import scipy.sparse as sparse
import random 

PATH = 'text8'



f = open(PATH, 'r')
line = f.readline()
f.close()

word_vocabs = line.split()
print 'number of words:', len(word_vocabs)
word_set = set([])
for word in word_vocabs:
    word_set.add(word)
print 'number of unique words:', len(word_set)

word_dict = {}
i = 0
for word in word_set:
    word_dict[word] = i
    i += 1

mtx = sparse.dok_matrix((len(word_set),len(word_set)))

window_size = 2
for pos, word_ in enumerate(word_vocabs):    
    reduced_window = random.randint(0, window_size)
    start = max(0, pos-window_size+reduced_window)
    for pos2, word2 in enumerate(word_vocabs[start:(pos + window_size + 1 - reduced_window)], start):
        if pos2 != pos:
            # print pos2, word2, word_vocabs[pos]
            mtx[word_dict[word2], word_dict[word_vocabs[pos]]] += 1

pair_list = [[edge, mtx[edge]] for edge in mtx.keys()]

fpairs = open('word_pairs.txt', 'w')
for i in pair_list:
    fpairs.write('%s %s %s\n' %(str(i[0][0]), str(i[0][1]), str(i[1])) )

fpairs.close()






