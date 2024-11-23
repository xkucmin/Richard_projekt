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


# fruits = ["apple", "banana", "cherry"]
#
# fruits.remove("apple")
# fruits.insert(1, "peach")
#
# for x in fruits:
#   print(x)

#Úloha 1: Deklarácia premenných a výpočet
#Vytvor premenné x a y, priraď im hodnoty 10 a 20. Vypočítaj ich súčet a rozdiel a vypíš výsledky.
from email.contentmanager import raw_data_manager

from torch.cpu import is_available


# x = 10
# y = 20
# sucet = x + y
# rozdiel = x - y
# print ("Súčet:",sucet)
# print ("Rozdiel:",rozdiel)

#Úloha 2: Základné operácie
#Napíš program, ktorý vypočíta obsah obdĺžnika so stranami a = 5 a b = 7. Vypíš výsledok vo formáte:
#Obsah obdĺžnika je: 35
# a = 5
# b = 7
# sucin = 5 * 7
# print ("Obsah obdĺžnika je :", sucin)

#Úloha 3: Jednoduchá funkcia
#Vytvor funkciu pozdrav(meno), ktorá vypíše pozdrav vo formáte:
#Ahoj, (meno)!
# def pozdrav(meno):
#     print ("Ahoj,", meno,"!")

#Úloha 4: Funkcia na matematickú operáciu
#Napíš funkciu vynasob(a, b), ktorá vypočíta súčin dvoch čísel a vráti výsledok. Zavolaj túto funkciu pre a = 4 a b = 6 a vypíš výsledok.
#Ak je výsledok záporný, pripocíta k výsledku císlo 100 a vráti vysledok
# def vynasob (a, b):
#     vysledok = a * b
#     if vysledok < 0:
#        vysledok = vysledok + 100
#     return vysledok
# a = 4
# b = 6
# vysledok = vynasob(a,b)
# print("Výsledok je:", vysledok)

#Úloha 5: Podmienky
#Napíš funkciu porovnaj(a, b), ktorá porovná dve čísla:

#Ak a je väčšie, vypíše: a je väčšie ako b.
#Ak b je väčšie, vypíše: b je väčšie ako a.
#Ak sú rovnaké, vypíše taký počet hviezdičiek, akú hodnotu má premenná a (alebo b, sú rovnaké).
#Zavolaj túto funkciu napríklad s hodnotami 5 a 10.
# def porovnaj (a, b):
#     if a > b:
#         print ("a je väčšie ako b")
#     if a < b:
#         print ("b je väčšie ako a")
#     if a == b:
#         print (a * "*")
# a = 5
# b = 10
#
# porovnaj(5,5)

#Úloha 6: Cyklus a výpis
#Vytvor funkciu hviezdicky(n), ktorá vypíše n riadkov hviezdičiek, pričom každý riadok obsahuje o jednu hviezdičku viac ako predchádzajúci.
#Napríklad, pre n = 4 je vzorovy vysledok v sprave nizsie
#Definícia funkcie hviezdicky
# def hviezdicky(n):
#     for i in range (n):  # tuto sa i zvacsuje od 0 do 3
#         print ( (i+1) * "*")
#
# hviezdicky(4)
#Úloha 7: Práca so zoznamom
#Vytvor funkciu pridaj(ovocie), ktorá pridá ovocie na koniec zoznamu. Funkciu, ktorá to robí najdes na internete (bude podobna ako ta, ktoru sme pouzivali).
# Polovica programovania je googlenie, tak nech si to uz vyskusas.
#Vo funkcie budes mat zoznam ovocia:
#fruits = ["apple", "banana", "cherry"]

#Pokial funkciu zavolas pridaj(orange), a potom vypises tento zoznam po pridaní, mal by vyzerat:
#fruits = ["apple", "banana", "cherry", "orange"]
# fruits = ["apple", "banana", "cherry"]
# def pridaj(ovocie):
#         fruits.append(ovocie)
#
# pridaj("orange")
# print(fruits)
# pozdrav("Adam")
# pozdrav("Richard")

