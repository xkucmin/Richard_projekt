from flask import Flask, request, jsonify, make_response
from entities.Pouzivatel import Pouzivatel
from entities.Autor import Autor
from entities.Kniha import Kniha
from entities.Vypozicka import Vypozicka
from functions.Funkcie import pridat_knihu, vypozicat_knihu, vratit_knihu, ziskat_knihy_podla_autora, ziskat_historiu_vypoziciek_knihy, nacitaj_vypozicky_z_db

app = Flask(__name__)

import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="password",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

# Load users
cur.execute("SELECT id, meno, email FROM pouzivatelia;")
pouzivatelia = [Pouzivatel(*row) for row in cur.fetchall()]

# Load authors
cur.execute("SELECT id, meno FROM autori;")
autori = [Autor(*row) for row in cur.fetchall()]

# Load books
def load_books():
    cur.execute("SELECT id, nazov, autor_id, dostupna FROM knihy;")
    knihy = [Kniha(*row) for row in cur.fetchall()]
    return knihy

# Load vypozicka
def load_vypozicka():
    cur.execute("SELECT kniha_id, pouzivatel_id, datum_vypozicky, datum_vratenia FROM vypozicky;")
    vypozicky = [Vypozicka(*row) for row in cur.fetchall()]
    return vypozicky

# pouzivatelia = [
#     Pouzivatel (1, "Jozef", "jozef@gmail.com"),
#     Pouzivatel(2, "Katka", "katka@gmail.com")
# ]
#
# autori = [
#     Autor(1, "J.K. Rowling"),
#     Autor(2, "William Shakespeare")
# ]
#
# knihy = [
#     Kniha(1, "Harry Potter a kameň mudrcov", 1),
#     Kniha(2, "Harry Potter a tajomná komnata", 1),
#     Kniha(3, "Hamlet", 2)
# ]

knihy = load_books()
@app.route('/pridat-knihu', methods=['POST'])
def pridat_knihu_endpoint():
    data = request.json
    nazov = data.get('nazov')
    autor_id = data.get('autor_id')

    if not nazov or not autor_id:
        return jsonify({"error": "Chýba 'nazov' alebo 'autor_id'"}), 400

    kniha = pridat_knihu(nazov, autor_id, conn, cur)
    return jsonify({"message": "Kniha pridaná", "kniha": kniha.__dict__})


@app.route('/vypozicat-knihu', methods=['POST'])
def vypozicat_knihu_endpoint():
    data = request.json
    kniha_id = data.get('kniha_id')
    pouzivatel_id = data.get('pouzivatel_id')

    if not kniha_id or not pouzivatel_id:
        return jsonify({"error": "Chýba 'kniha_id' alebo 'pouzivatel_id'"}), 400
    vypozicky = load_vypozicka()

    if vypozicat_knihu(knihy, vypozicky, kniha_id, pouzivatel_id, conn, cur):
        return jsonify({"message": "Kniha bola úspešne vypožičaná"})
    return jsonify({"error": "Kniha nie je dostupná alebo neexistuje"}), 400


@app.route('/vratit-knihu', methods=['POST'])
def vratit_knihu_endpoint():
    data = request.json
    vypozicka_id = data.get('vypozicka_id')

    if not vypozicka_id:
        return jsonify({"error": "Chýba 'vypozicka_id'"}), 400

    vypozicky = load_vypozicka()
    if vratit_knihu(knihy, vypozicky, vypozicka_id, conn, cur):  #Zistiť prečo to nejde
        return jsonify({"message": "Kniha bola úspešne vrátená"})
    return jsonify({"error": "Výpožička neexistuje alebo už bola vrátená"}), 400

@app.route('/ziskat-vypozicky', methods=['GET'])
def ziskat_vypozicky_endpoint():
    cur.execute("SELECT id, kniha_id, pouzivatel_id, datum_vypozicky, datum_vratenia FROM vypozicky;")
    vypozicky = [Vypozicka(*row) for row in cur.fetchall()]
    data = [vypozicka.to_dict2() for vypozicka in vypozicky]
    response = jsonify(data)
    return response, 200

#@app.route('/ziskat-knihy', methods=['GET'])
#def ziskat_knihy_endpoint():
#    cur.execute("SELECT id, nazov, autor_id FROM knihy;")
#    knihy = [Kniha(*row) for row in cur.fetchall()]
#    data = [kniha.to_dict() for kniha in knihy]
#    response = jsonify(data)
#    return response, 200

@app.route('/ziskat-knihy', methods=['GET'])
def ziskat_knihy():
    vypozicky = nacitaj_vypozicky_z_db(cur)
    knihy_data = []

    for kniha in knihy:
        vypozicana = any(
            v.kniha_id == kniha.id and v.datum_vratenia is None
            for v in vypozicky
        )
        knihy_data.append({
            "id": kniha.id,
            "nazov": kniha.nazov,
            "autor": kniha.autor,
            "dostupna": not vypozicana
        })

    return jsonify(knihy_data)


@app.route('/knihy-podla-autora', methods=['POST'])
def knihy_podla_autora_endpoint():
    data = request.json
    meno_autora = data.get('meno_autora')

    if not meno_autora:
        return jsonify({"error": "Chýba 'meno_autora'"}), 400

    knihy_autora = ziskat_knihy_podla_autora(meno_autora, conn, cur)

    if knihy_autora is None:
        return jsonify({"error": "Autor neexistuje"}), 404

    return jsonify({"autor": meno_autora, "knihy": knihy_autora}), 200

#podobne ako knihy-pdola-autora,
@app.route('/historia-vypoziciek-knihy', methods=['GET'])
def historia_vypoziciek_knihy_endpoint():
    kniha_id = request.args.get('kniha_id', type=int)

    if kniha_id is None:
        return jsonify({"error": "Chýba 'kniha_id' parameter"}), 400

    historia = ziskat_historiu_vypoziciek_knihy(kniha_id, conn, cur)

    if not historia:
        return jsonify({"message": "Žiadna výpožička pre danú knihu"}), 404

    return jsonify(historia), 200

if __name__ == '__main__':
    app.run(debug=True)

