class Person:
  def __init__(self, id, name, year):
    self.id = id
    self.name = name
    self.year = year

class Car:
    def __init__(self, id, name, year):
        self.id = id
        self.name = name
        self.year = year

class Owns_Car:
    def __init__(self, id_person, id_car):
        self.id_person = id_person
        self.id_car = id_car

# class Product:
#   def __init__(self, id, name, author, number_of_pages, available):
#     self.id = id
#     self.name = name
#     self.author = author
#     self.number_of_pages = number_of_pages
#     self.available = available

# # spravit funkciu, ktora ma ako vstup vsetky knihy a my chceme vratit iba tie, ktore su dostupne
# def get_available_books(book_list):
#     available_books = []
#     for book in book_list:
#         if book.number_of_pages == 1000 and book.author == "richard":
#             book.name = 'new'
#             available_books.append(book)
#     return available_books
#
# book1 = Book(1, "book1", "adam", 100, True)
# book2 = Book(2, "book2", "richard", 1000, False)
# book3 = Book(3, "book3", "richard", 1000, True)
# book4 = Book(4, "book4", "adam", 100, False)
#
# books = [book1, book2, book3, book4]
# for book in books:
#     print(book.name)
# my_books = get_available_books(books)
auto1 = Car(1, "Skoda Octavia", 2005)
auto2 = Car(2, "Ford Fiesta", 2010)
cars = [auto1, auto2]

adam = Person(1, "adam", 2000)
richard = Person(2, "richard", 2000)
persons = [adam, richard]

vztah_1 = Owns_Car(1,1)  # vztah ktory nam hovori o tom, aka osoba (jej id) vlastni ake auto (jej id)
vztah_2 = Owns_Car(1, 2)
vztahy = [vztah_1, vztah_2]

def get_person_car(person, cars, vztahy_list):
    person_cars_ids = []
    for vztah in vztahy_list:                # prechadzame vsetky vztahy osoby a auta, teda objekty Owns_Car
        if vztah.id_person == person.id:     # ak id_osoby v owns_car = id_osoby ktorej auto hladame, splni sa tato podmienka
            id_car = vztah.id_car            # zo vztahy si vyberieme id auta, ktore tato osoba vlastni
            person_cars_ids.append(id_car)   # a pridame ho do listu
    print(person_cars_ids)

get_person_car(adam, cars, vztahy)
