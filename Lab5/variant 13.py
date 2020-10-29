colors = ['жовтий', 'червоний', 'зелений', 'синій']
keywords = ['жовт', 'червон', 'зелен', 'син']

text = 'Жовтий півник та червоний олень дивилися на червоне сонце та синє небо'

counter = 0
while True:
    if keywords in text:
        counter += 1

def total_amout_of_words_in_file():
    num_words = 0
    words_set = set()  # количество слов
    
    num_keywords = set() #слова, которые включают корни слов у цветов
    words_array = []

    with open(text, 'r') as f:
        for line in f:

            words = line.split()
            num_words += len(words)

            for word in words:
                words_set.add(word)
                words_array.append(word)

    for i in range(0, len(words_array)):
        if(words_array.count(words_array[i]) == 1):
            num_keywords.add(words_array[i])

    print(f'Количество слов {len(words_set)}')
    print(f'Количество слов, которые в первый раз встретились {len(num_keywords)}')

    return num_words

print(f'Количество слов в файле {total_amout_of_words_in_file()}')

