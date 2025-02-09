from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Objekty v systéme

class Pouzivatel:
    def __init__(self, id, meno, email):
        self.id = id
        self.meno = meno
        self.email = email

class Kniha:
    def __init__(self, id, nazov, autor_id, dostupna):
        self.id = id
        self.nazov = nazov
        self.autor_id = autor_id
        self.dostupna = dostupna

class Autor:
    def __init__(self, id, meno):
        self.id = id
        self.meno = meno

class Vypozicka:
    def __init__(self, id, kniha_id, pouzivatel_id, datum_vypozicky, datum_vratenia=None):
        self.id = id
        self.kniha_id = kniha_id
        self.pouzivatel_id = pouzivatel_id
        self.datum_vypozicky = datum_vypozicky
        self.datum_vratenia = datum_vratenia

# Implementácia a testovanie
pouzivatelia = [
    Pouzivatel(1, "Jozef", "jozef@gmail.com"),
    Pouzivatel(2, "Katka", "katka@gmail.com")
]

autori = [
    Autor(1, "J.K. Rowling"),
    Autor(2, "William Shakespeare")
]

knihy = [
    Kniha(1, "Harry Potter a kameň mudrcov", 1, True),
    Kniha(2, "Harry Potter a tajomná komnata", 1, True),
    Kniha(3, "Hamlet", 2, True)
]

vypozicky = []

# Funkcionalita systému

@app.route('/pridat-knihu', methods=['POST'])
def pridat_knihu_endpoint():
    data = request.json
    if 'nazov' not in data or 'autor_id' not in data:
        return jsonify({"error": "Chýbajúce údaje"}), 400
    nova_kniha = Kniha(len(knihy) + 1, data['nazov'], data['autor_id'], True)
    knihy.append(nova_kniha)
    return jsonify({"message": "Kniha pridaná"}), 201

@app.route('/knihy-autora/<int:autor_id>', methods=['GET'])
def ziskat_knihy_autora_endpoint(autor_id):
    knihy_autora = [k.nazov for k in knihy if k.autor_id == autor_id]
    return jsonify({"knihy": knihy_autora})

@app.route('/vypozicat-knihu', methods=['POST'])
def vypozicat_knihu_endpoint():
    data = request.json
    if 'kniha_id' not in data or 'pouzivatel_id' not in data:
        return jsonify({"error": "Chýbajúce údaje"}), 400
    kniha_id = data['kniha_id']
    pouzivatel_id = data['pouzivatel_id']
    for kniha in knihy:
        if kniha.id == kniha_id and kniha.dostupna:
            kniha.dostupna = False
            vypozicky.append(Vypozicka(len(vypozicky) + 1, kniha_id, pouzivatel_id, datetime.now(), None))
            return jsonify({"message": "Kniha vypožičaná"})
    return jsonify({"error": "Kniha nie je dostupná"}), 400

@app.route('/vratit-knihu', methods=['POST'])
def vratit_knihu_endpoint():
    data = request.json
    if 'vypozicka_id' not in data:
        return jsonify({"error": "Chýbajúce údaje"}), 400
    vypozicka_id = data['vypozicka_id']
    for vypozicka in vypozicky:
        if vypozicka.id == vypozicka_id and vypozicka.datum_vratenia is None:
            vypozicka.datum_vratenia = datetime.now()
            for kniha in knihy:
                if kniha.id == vypozicka.kniha_id:
                    kniha.dostupna = True
            return jsonify({"message": "Kniha vrátená"})
    return jsonify({"error": "Neplatná výpožička"}), 400

@app.route('/zoznam-knih-pouzivatela/<int:pouzivatel_id>', methods=['GET'])
def zoznam_knih_pouzivatela_endpoint(pouzivatel_id):
    knihy_pouzivatela = []
    for vypozicka in vypozicky:
        if vypozicka.pouzivatel_id == pouzivatel_id and vypozicka.datum_vratenia is None:
            for kniha in knihy:
                if kniha.id == vypozicka.kniha_id:
                    knihy_pouzivatela.append(kniha.nazov)
    return jsonify({"knihy": knihy_pouzivatela})

if __name__ == '__main__':
    app.run(debug=True)
