import os

book = "Гаррі Поттер і філософський камінь.txt"
test = "test.txt"
filename = book
os.chdir('Lab5')

def count_total_amout_of_chars_with_spaces():

    file = open(filename, 'r')

    data = file.read()
    total_amount = len(data)

    file.close()

    return total_amount

def count_total_amout_of_chars_without_spaces():

    num_chars = 0

    with open(filename, 'r') as f:
        for line in f:
            for letter in line:
                for i in letter:
                    if(i != ' ' and i != '\n'):
                        num_chars += 1

    return num_chars

def total_amout_of_words_in_file():
    num_words = 0
    words_set = set()  # количество разных слов
    
    one_time_words = set() #слова, которые в первый раз
    words_array = []

    with open(filename, 'r') as f:
        for line in f:

            words = line.split()
            num_words += len(words)

            for word in words:
                words_set.add(word)
                words_array.append(word)

    for i in range(0, len(words_array)):
        if(words_array.count(words_array[i]) == 1):
            one_time_words.add(words_array[i])

    print(f'Количество слов {len(words_set)}')
    print(f'Количество слов, которые в первый раз встретились {len(one_time_words)}')

    return num_words

print(f'С пробелами {count_total_amout_of_chars_with_spaces()}')
print(f'Без пробелов {count_total_amout_of_chars_without_spaces()}')
print(f'Количество слов в файле {total_amout_of_words_in_file()}')
