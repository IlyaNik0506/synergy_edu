text = input("Введите предложение: ")
words = text.split()


un_word = {}
for word in words:
    if word in un_word:
        un_word[word] += 1
    else:
        un_word[word] = 1
for word, number in un_word.items():
    print(f'{word} повторяется: {number} раз')
