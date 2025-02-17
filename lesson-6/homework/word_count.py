import string
from Tools.demo.spreadsheet import translate


try:
    with open('sample.txt', 'r') as file:
        my_file = file.read()
except FileNotFoundError:
    print('File not found, let\'s create it')
    my_file = input('Type your file here: ')
    with open('sample.txt', 'w') as file:
        file.write(my_file)

word_count = {}
with open('sample.txt', 'r') as file:
    my_file = file.read()
    my_file = my_file.translate(str.maketrans('', '', string.punctuation))
    words = my_file.split()
    for word in words:
        word = word.lower()
        if word in word_count:
                word_count[word] += 1
        else:
                word_count[word] = 1

for word, count in word_count.items():
                print(f'{word}: {count} \n', end='')

