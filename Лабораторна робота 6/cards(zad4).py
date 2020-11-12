from dataclasses import dataclass
import random

suits = ['diamonds', 'hearts','spades', 'clubs']

@dataclass
class Card:
    suit: str
    number: int


class CardPack():

    def __init__(self):
        self.card_pack_array = []

        for suit in suits:
            for card in self.create_suit_pack(suit):
                self.card_pack_array.append(card)

        random.shuffle(self.card_pack_array)

    #Метод, за допомогою якого ми створюємо масив, в якому будуть зберігатися наші масті
    def create_suit_pack(self, suit_name):
        suit_pack = []
        for i in range(6, 14):
            suit_pack.append(Card(suit_name, i))

        return suit_pack

    #Метод, за допомогою якого ми виводимо на екран гравцю всі його(її) карти
    def print_card_pack(self):
        print('Вивести усі карти ' + str(self.card_pack_array))

    def get_card_by_id_in_pack(self, id):
        return self.card_pack_array[id - 1]

    #Метод, за допомогою якого ми перетасовуємо колоду
    def shuffle_pack(self):
        random.shuffle(self.card_pack_array)

    #Метод, за допомогою якого ми надаємо гравцю одну карту з колоди
    def get_one_card(self):
        card = self.card_pack_array[0]
        self.card_pack_array.remove(card)

        return card

    #Метод, за допомогою якого ми надаємо гравцю шість карт зколоди
    def get_six_cards(self):
        six_cards_pack = [
            self.card_pack_array[0],
            self.card_pack_array[1],
            self.card_pack_array[2],
            self.card_pack_array[3],
            self.card_pack_array[4],
            self.card_pack_array[5],
        ]

        for card in six_cards_pack:
            self.card_pack_array.remove(card)

        return six_cards_pack


card_pack = CardPack()
card_pack.print_card_pack()
print('\n')
print('Отримайте четверту карту з колоди ' + str(card_pack.get_card_by_id_in_pack(4)) + "\n")
card_pack.print_card_pack()
print('\n')
print('Перетасувати картки \n')
card_pack.shuffle_pack()
card_pack.print_card_pack()
print('\n')
print('Отримайте одну карту ' + str(card_pack.get_one_card()) + '\n')
print('Отримайте шість карт ' + str(card_pack.get_six_cards()))