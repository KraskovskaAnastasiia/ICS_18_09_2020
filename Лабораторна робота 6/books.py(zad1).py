from dataclasses import dataclass

commands = ["Додати книгу", "Видалити книгу", "Книга за номером", "Знайти книгу", "Зупинитися",
            "Вивести на екран усі книги", ]


@dataclass
class Book:
    book_name: str
    author: str
    genre: str
    year_of_publishing: int
    book_id: int


test_books_list = [
    Book("Гаррі Поттер і філософський камінь", "Джоан Роулінг", "фентезі ", 1997, 1),
    Book("Я захищу тебе", "Світлана Талан", "роман", 2019, 2),
    Book("Звіяні вітром", "Маргарет Мітчел", "роман-епопея", 1939, 3),
]


def print_book(book):
    print("\nНазва: {book_name}\nАвтор: {author}\nЖанр: {genre}\nРык: {year_of_publishing}\nНомер: {book_id}".format(book_name=book.book_name,
                                                                                                                                   author=book.author, genre=book.genre, year_of_publishing=book.year_of_publishing, book_id=book.book_id))


class Library():

    def __init__(self):
        self.books = []

    def add_book(self, book_name, author, genre, year_of_publishing):
        id = 0

        if(len(self.books) != 0):
            id = len(self.books) + 1

        self.books.append(Book(book_name, author, genre,
                               year_of_publishing, id))

    def add_book_object(self, book):
        self.books.append(book)

    def delete_book(self, book_id):
        for book in self.books:
            if(book.book_id == book_id):
                self.books.remove(book)
                print("Книга видалена")
                print_book(book)

    def print_all_books(self):
        for book in self.books:
            print_book(book)

    def get_book_by_id(self, id):
        for book in self.books:
            if(book.book_id == id):
                print_book(book)

    def search_book(self, query_dict):

        found_books = []

        for book in self.books:

            if(query_dict['назва'] == book.book_name or
               query_dict['автор'] == book.author or
               query_dict['жанр'] == book.genre or
               query_dict['рік'] == book.year_of_publishing or
               query_dict['id'] == book.book_id):

                found_books.append(book)

        if(len(found_books) == 0):
            print("Sorry, but we didn't find the book")
        else:
            for found_book in found_books:
                print_book(found_book)

library = Library()
print("Ви у бібліотеці")
for test_book in test_books_list:
    library.add_book_object(test_book)

while True:

    print("Доступні комманди для Вашого використання: " + str(commands))
    command = input("Введіть бажану комманду: ")

    # У цьому блоці коду ми додаємо книгу у нашу бібліотеку
    if command == commands[0]:

        book_name = input("Назва: ")
        author = input("Автор: ")
        genre = input("Жанр: ")
        year_of_publishing = int(input("Рік: "))

        library.add_book(book_name, author, genre, year_of_publishing)

    # У цьому блоці коду ми видаляємо книгу з нашої бібліотеки
    elif command == commands[1]:
        book_id = int(input("Номер: "))
        library.delete_book(book_id)

    # У цьому блоці коду ми шукаємо книгу у нашій бібліотеці за допомогою унікального номера
    elif command == commands[2]:
        book_id = input("Номер: ")
        if(book_id != ''):
            library.get_book_by_id(int(book_id))
        else:
            print("Не обрано номер киги")

    # У цьому блоці коду ми шукаємо книгу у нашій бібліотеці
    elif command == commands[3]:
        book_name = input(" Назва: ")
        author = input("Автор: ")
        genre = input("Жанр: ")
        year_of_publishing = input(" Рік: ")
        book_id = input("Номер: ")

        if(book_id != ''):
            book_id = int(book_id)

        if(year_of_publishing != ''):
            year_of_publishing = int(year_of_publishing)

        query = {'Назва': book_name, 'автор': author, 'жанр': genre,
                 'рік': year_of_publishing, 'номер': book_id}
        library.search_book(query)

    # У цьому блоці коду ми зупиняємо роботу з пошуку книги у нашій бібліотеці
    elif command == commands[4]:
        print("До нових зустрічей!")
        break

    # У цьому блоці коду ми виводимо на екран усі книги у нашій бібліотеці
    elif command == commands[5]:
        library.print_all_books()

    # У цьому блоці коду ми виводимо на екран усі книги у нашій бібліотеці
    else:
        library.print_all_books()


def main():
    return 0


if __name__ == '__main__':
    main()