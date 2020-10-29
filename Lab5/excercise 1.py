import random

name = ['Олесь', 'Іванна', 'Віктор', 'Мирон']
state = ['хоче', 'полюбляє', 'обожнює', 'ненавидить' ]
action = ['гуляти', 'гратися з собакою', 'дивитися на зірки', 'читати книжки', 'малювати']

random_list = [name, state, action]


def random_phrase():
    result_string = ""
    for i in range(0, 3):
        random_index = random.randrange(0, 4)
        result_string = result_string + \
            random_list[i][random_index] + " "

    return result_string

print(random_phrase())