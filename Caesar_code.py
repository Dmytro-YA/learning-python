way = input('What would you like me to do, code/decode?:')
language = input('What language would you like me to do, russian/english?:')
step = int(input('How much will be a step?:'))

russian_upper = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
russian_lower = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
english_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
english_lower = 'abcdefghijklmnopqrstuvwxyz'

if way == 'code' and language == 'russian':
    sentence_to_code = input('Put here text to code:')
    coded_sentence = ''
    for i in sentence_to_code:
        if i in russian_upper:
            needed_char = (russian_upper.index(i) + step) % 32
            coded_char = russian_upper[needed_char]
            coded_sentence += coded_char
        elif i in russian_lower:
            needed_char = (russian_lower.index(i) + step) % 32
            coded_char = russian_lower[needed_char]
            coded_sentence += coded_char
        else:
            coded_sentence += i

if way == 'code' and language == 'english':
    sentence_to_code = input('Put here text to code:')
    coded_sentence = ''
    for i in sentence_to_code:
        if i in english_upper:
            needed_char = (english_upper.index(i) + step) % 26
            coded_char = english_upper[needed_char]
            coded_sentence += coded_char
        elif i in english_lower:
            needed_char = (english_lower.index(i) + step) % 26
            coded_char = english_lower[needed_char]
            coded_sentence += coded_char
        else:
            coded_sentence += i

if way == 'decode' and language == 'russian':
    sentence_to_decode = input('Put here text to decode:')
    coded_sentence = ''
    for i in sentence_to_decode:
        if i in russian_upper:
            needed_char = (russian_upper.index(i) - step) % 32
            coded_char = russian_upper[needed_char]
            coded_sentence += coded_char
        elif i in russian_lower:
            needed_char = (russian_lower.index(i) - step) % 32
            coded_char = russian_lower[needed_char]
            coded_sentence += coded_char
        else:
            coded_sentence += i
if way == 'decode' and language == 'english':
    sentence_to_decode = input('Put here text to decode:')
    coded_sentence = ''
    for i in sentence_to_decode:
        if i in english_upper:
            needed_char = (english_upper.index(i) - step) % 26
            coded_char = english_upper[needed_char]
            coded_sentence += coded_char
        elif i in english_lower:
            needed_char = (english_lower.index(i) - step) % 26
            coded_char = english_lower[needed_char]
            coded_sentence += coded_char
        else:
            coded_sentence += i
print(coded_sentence)
