from flask import Flask, request, jsonify
from entities.Pouzivatel import Pouzivatel
from entities.Autor import Autor
from entities.Kniha import Kniha
from functions.Funkcie import pridat_knihu, vypozicat_knihu, vratit_knihu

app = Flask(__name__)

pouzivatelia = [
    Pouzivatel (1, "Jozef", "jozef@gmail.com"),
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

@app.route('/pridat-knihu', methods=['POST'])
def pridat_knihu_endpoint():
    data = request.json
    nazov = data.get('nazov')
    autor_id = data.get('autor_id')

    if not nazov or not autor_id:
        return jsonify({"error": "Chýba 'nazov' alebo 'autor_id'"}), 400

    kniha = pridat_knihu(nazov, autor_id)
    return jsonify({"message": "Kniha pridaná", "kniha": kniha.__dict__})


@app.route('/vypozicat-knihu', methods=['POST'])
def vypozicat_knihu_endpoint():
    data = request.json
    kniha_id = data.get('kniha_id')
    pouzivatel_id = data.get('pouzivatel_id')

    if not kniha_id or not pouzivatel_id:
        return jsonify({"error": "Chýba 'kniha_id' alebo 'pouzivatel_id'"}), 400

    if vypozicat_knihu(kniha_id, pouzivatel_id):
        return jsonify({"message": "Kniha bola úspešne vypožičaná"})
    return jsonify({"error": "Kniha nie je dostupná alebo neexistuje"}), 400


@app.route('/vratit-knihu', methods=['POST'])
def vratit_knihu_endpoint():
    data = request.json
    vypozicka_id = data.get('vypozicka_id')

    if not vypozicka_id:
        return jsonify({"error": "Chýba 'vypozicka_id'"}), 400

    if vratit_knihu(vypozicka_id):
        return jsonify({"message": "Kniha bola úspešne vrátená"})
    return jsonify({"error": "Výpožička neexistuje alebo už bola vrátená"}), 400


if __name__ == '__main__':
    app.run(debug=True)
