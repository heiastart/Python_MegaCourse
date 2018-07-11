import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        print(word.title())
        return data[word.title()]
    elif word.upper() in data:
        print(word.upper())
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        y_n = input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(word, data.keys())[0])
        if y_n == 'Y' or y_n == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif y_n == 'N' or y_n == 'n':
            return 'Word not in dictionary. Try again!'
        else:
            return 'Invalid input.'
    else:
        return 'Word not in dictionary. Try again!'

inputWord = input('Word to look up: ')
output = translate(inputWord)
#print(translate(inputWord))

if type(output) == list:
    for i in output:
        print('-', i)
else:
    print(output)


'''
OR WITH TRY-EXCEPT BLOCK:
try:
    print(translate(inputWord))
except KeyError:
    print('Word not in dictionary. Try again!')
'''