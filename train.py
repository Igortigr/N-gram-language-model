import codecs
import pickle
import numpy as np
import string


class N_gram:
    finish_dict = {}
    list_words = ''

    def fit(self, text, n):
        table = str.maketrans('', '', string.punctuation)
        self.list_words = [w.translate(table).lower() for w in text.split()]
        length_list_words = len(self.list_words)
        N = [tuple(self.list_words[i:i + n]) for i in range(length_list_words) if len(self.list_words[i:i + n]) == n]
        d = self.count_words(self.list_words)
        words = self.count_words(N)
        for i in words:
            words[i] = words[i] / d[i[0]]
        list_p = []
        list_w = []
        for i_word in self.list_words:
            for key_word, value_word in words.items():
                if i_word == key_word[0]:
                    list_p.append(value_word)
                    list_w.append(key_word[1])
                    self.finish_dict[i_word] = {tuple(list_w): tuple(list_p)}
            list_p = []
            list_w = []
        return self.finish_dict

    def count_words(self, List):
        words = {}
        for word in List:
            if word not in words:
                words[word] = 1
            else:
                words[word] += 1
        return words

    def predict(self, word):
        global k
        if word in self.finish_dict:
            for j1, j2 in self.finish_dict.get(word).items():
                key_j = j1
                p_j = j2
                k = np.random.choice(key_j, p=p_j)
        else:
            k = None
        return k


with codecs.open('data.txt', 'r') as f:
    text = f.read()
Ngram = N_gram()
Ngram.fit(text, 2)
with open('model.pkl', 'wb') as f:
    pickle.dump(Ngram, f)
