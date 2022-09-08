import pickle
import random
from train import N_gram
with open('model.pkl', 'rb') as f:
    data_new = pickle.load(f)

finish_text = ''
try:
    n = int(input('Какова длина строки? '))
except ValueError:
    n = random.randint(2, 10)
word = input('Напишите первое слово: ')
if word == '':
    word = random.choice(data_new.list_words)
for i in range(n):
    if len(word.split()) != 1:
        word = word.split()[-1]
    finish_text += word + ' '
    word = data_new.predict(word)
print('Сгенерированная строка: ', finish_text)