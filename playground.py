# dnes prejdeme deklaraciu premennych,
# zakladne matematicke operacie, vypisy a vytvorenie a zavolanie jednoduchej funkcie
# co je to premenna?
from dataclasses import asdict

from setuptools.command.sdist import sdist


# def zrataj(a, b):
#     c = a + b
#     return c

# kolkokrat = 50 # toto je deklaracia
# nieco = 5

# vysledok = kolkokrat * nieco
# vysledok = vysledok + 1

# vysledok2 = zrataj(2,4)

#cyklus - klucove slovo je for
#spravime funkciu, do ktorej pojdu 2 atributy (a, b)
# a bude oznacovat pocet hviezdieciek v riadku
# b bude oznacovat, kolko tych riadkov bude
# def funkcia(a,b):
#     for i in range (b):
#         print(a*'*')

#funkcia(3,5)

# podmienka = klucove slovo je if
# vystupom z podmienky je vzdy pravdivostna hodnota : true/false
#spravime funkciu, do ktorej pojdu 2 atributy (a, b)
# ak je hodnota a > hodnota b, sprav a*b
# ak je hodnota a < hodnota b, srpav a+b
# ak je rovnaka, nesprav nic, iba vypis ze sa cisla rovnaju
# def porovnanie(a,b):
#     if a > b:
#         c = a * b
#     if a < b:
#         c = a + b
#     if a == b:
#         c = 'Cisla su rovnake'
#     print (c)
#
# porovnanie(5,5)


fruits = ["apple", "banana", "cherry"]

fruits.remove("apple")
fruits.insert(1, "peach")

for x in fruits:
  print(x)