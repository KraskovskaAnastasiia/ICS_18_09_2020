import matplotlib.pyplot as plt
import pylab

text = 'Привіт! Як Ваші справи? Це ж Чудово... Я люблю Сонечко. А Ти? Ох, яка Краса... Я Тебе Кохаю! А Ти поснідав сьогодні? Я Завжди Буду Поруч! '
signs = ['!', '?', '...', '.']

sentence_types = {}
known = 0

for index, char in enumerate(text):
    if known != 0:
        known = known - 1
        continue
    if char in signs:

        if char == '.':

            if index != len(text) - 2:

                if text[index + 1] == '.' and text[index + 2] == '.':

                    try:
                        frequency = sentence_types['...']
                        frequency += 1
                        sentence_types['...'] = frequency
                    except:
                        sentence_types['...'] = 1
                        print("except")

                    known = 2

                else:

                    try:
                        frequency = sentence_types[char]
                        sentence_types['.'] = frequency + 1
                    except:
                        sentence_types['.'] = 1
        else:
            try:
                frequency = sentence_types[char]
                sentence_types[char] = frequency + 1
            except:
                sentence_types[char] = 1

print(sentence_types)

xdata = []
ydata = []
letter_values = []

for frequency in sentence_types:
    try:
        xdata.append(xdata[len(xdata) - 1] + 1)
    except:
        xdata.append(0)

    ydata.append(sentence_types[frequency])
    letter_values.append(frequency)

pylab.bar(xdata, ydata, width=0.5, color=['b', 'c', 'g', 'm', 'r'])
plt.xlabel('Знак')
plt.ylabel('Частота')
plt.xticks(xdata, letter_values)
plt.title('Типи речень у тесті')

pylab.show()