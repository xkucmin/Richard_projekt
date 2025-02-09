from entities.Kniha import Kniha
from entities.Vypozicka import Vypozicka
from entities.Autor import Autor
from entities.Pouzivatel import Pouzivatel
from functions.Funkcie import pridat_knihu, vypozicat_knihu, vratit_knihu


pouzivatelia = [
    Pouzivatel(1, "Jozef", "jozef@gmail.com"),
    Pouzivatel(2, "Katka", "katka@gmail.com")
]

autori = [
    Autor(1, "J.K. Rowling"),
    Autor(2, "William Shakespeare")
]

knihy = [
    Kniha(1, "Harry Potter a kameň mudrcov", 1),
    Kniha(2, "Harry Potter a tajomná komnata", 1),
    Kniha(3, "Hamlet", 2)
]

vypozicky = []


nova_kniha = pridat_knihu(knihy, "Nová Kniha", 1)
print(f"Pridaná kniha: {nova_kniha.nazov}")


if vypozicat_knihu(knihy, vypozicky, 1, 1):
    print("Kniha úspešne vypožičaná.")
else:
    print("Kniha nie je dostupná.")


if vratit_knihu(knihy, vypozicky, 1):
    print("Kniha bola úspešne vrátená.")
else:
    print("Chyba pri vrátení knihy.")
