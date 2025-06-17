# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
print(word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'
glasn = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
letter_count = 0
for letter in glasn:
    letter_count += word.lower().count(letter)
print(letter_count)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
word_count = 0
for say in sentence.split():
    word_count += 1
print(word_count)

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
for say in sentence.split():
    print(say[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
word_count = 0
letter_count = 0
for say in sentence.split():
    word_count += 1
    letter_count += len(say)
print(letter_count / word_count)
