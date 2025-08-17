from flask import jsonify

from entities.Kniha import Kniha
from entities.Vypozicka import Vypozicka
from entities.Autor import Autor
from entities.Pouzivatel import Pouzivatel

def pridat_knihu(nazov, autor_id, conn, cur):

    # Insert book and get generated ID
    cur.execute(
        "INSERT INTO knihy (nazov, autor_id) VALUES (%s, %s) RETURNING id",
        (nazov, autor_id)
    )
    kniha_id = cur.fetchone()[0]

    conn.commit()

    return Kniha(kniha_id, nazov, autor_id)

from datetime import datetime

#def vypozicat_knihu(knihy, vypozicky, kniha_id, pouzivatel_id, conn, cur):
#    for kniha in knihy:
#        if kniha.id == kniha_id and kniha.dostupna:
#            kniha.vypozicat(conn, cur)
#
#            cur.execute(
#                "INSERT INTO vypozicky (kniha_id, pouzivatel_id, datum_vypozicky) VALUES (%s, %s, %s) RETURNING id",
#                (kniha_id, pouzivatel_id, datetime.now())
#            )
#            vypozicka_id = cur.fetchone()[0]
#            conn.commit()
#
#            nova_vypozicka = Vypozicka(vypozicka_id, kniha_id, pouzivatel_id, datetime.now())
#
#            vypozicky.append(nova_vypozicka)
#            return True
#    return False

def vypozicat_knihu(knihy, vypozicky, kniha_id, pouzivatel_id, conn, cur):
    vypozicky = nacitaj_vypozicky_z_db(cur)

    for vypozicka in vypozicky:
        if vypozicka.kniha_id == kniha_id and vypozicka.datum_vratenia is None:
            return False

    for kniha in knihy:
        if kniha.id == kniha_id:
            kniha.vypozicat(conn, cur)

            cur.execute(
                "INSERT INTO vypozicky (kniha_id, pouzivatel_id, datum_vypozicky) VALUES (%s, %s, %s)",
                (kniha_id, pouzivatel_id, datetime.now())
            )
            conn.commit()
            return True

    return False

#riadok 25 ako INSERT INTO vypozicky + kniha_id, ... lenvyozicky +1 netreba

def vratit_knihu(knihy, vypozicky, vypozicka_id, conn, cur):
    for vypozicka in vypozicky:
        if vypozicka.id == vypozicka_id and vypozicka.datum_vratenia is None:
            vypozicka.vratit(datetime.now(), conn, cur)
            for kniha in knihy:
                print (kniha.id)
                if kniha.id == vypozicka.kniha_id:
                    print (kniha.id)
                    kniha.vratit(conn, cur)
                    return True
    return False

#def ziskat_knihy_podla_autora(knihy, autori, meno_autora, conn, cur):
    # cur.execute("SELECT * FROM vypozicky WHERE autor_id = %s;")
    # vypozicky = [Vypozicka(*row) for row in cur.fetchall()]
    # data = [vypozicka.to_dict2() for vypozicka in vypozicky]
    # return data

def ziskat_knihy_podla_autora(meno_autora, conn, cur):
    cur.execute("SELECT id FROM autori WHERE meno = %s", (meno_autora,))
    autor_row = cur.fetchone()

    if autor_row is None:
        return []

    autor_id = autor_row[0]

    cur.execute("SELECT * FROM knihy WHERE autor_id = %s", (autor_id,))
    knihy = [Kniha(*row) for row in cur.fetchall()]
    data = [kniha.to_dict() for kniha in knihy]

    return data

#def ziskat_historiu_vypoziciek_knihy(vypozicky, pouzivatelia, kniha_id):
#    historia = []
#    for vypozicka in vypozicky:
#        if vypozicka.kniha_id == kniha_id:
#            pouzivatel = next((p for p in pouzivatelia if p.id == vypozicka.pouzivatel_id), None)
#            if pouzivatel:
#                historia.append({
#                    "meno": pouzivatel.meno,
#                    "datum_vypozicky": vypozicka.datum_vypozicky.isoformat() if vypozicka.datum_vypozicky else None,
#                    "datum_vratenia": vypozicka.datum_vratenia.isoformat() if vypozicka.datum_vratenia else None
#                })
#    return historia


def ziskat_historiu_vypoziciek_knihy(kniha_id, conn, cur):
    historia = []

    cur.execute("SELECT pouzivatel_id, datum_vypozicky, datum_vratenia FROM vypozicky WHERE kniha_id = %s", (kniha_id,))
    vypozicky_rows = cur.fetchall()

    for row in vypozicky_rows:
        pouzivatel_id, datum_vypozicania, datum_vratenia = row

        cur.execute("SELECT meno FROM pouzivatelia WHERE id = %s", (pouzivatel_id,))
        pouzivatel_row = cur.fetchone()

        meno = pouzivatel_row[0] if pouzivatel_row else "Neznámy"

        historia.append({
            "meno": meno,
            "datum_vypozicky": datum_vypozicania.isoformat() if datum_vypozicania else None,
            "datum_vratenia": datum_vratenia.isoformat() if datum_vratenia else None
        })
    print (historia)
    return (historia)

def nacitaj_vypozicky_z_db(cur):
    cur.execute("SELECT id, kniha_id, pouzivatel_id, datum_vypozicky, datum_vratenia FROM vypozicky")
    rows = cur.fetchall()
    vypozicky = []
    for row in rows:
        vypozicky.append(Vypozicka(row[0], row[1], row[2], row[3], row[4]))
    return vypozicky

#miesto riadkov 73 a 74 podobne ako riadok 58 Select from vypozicky = ...
#z vypozicky si vyberiem pouzivatel.id tak ako riadok 75, potom select from pouzivatel where pouzivatel id = %s
#riadky 76 - 81   (riadky 72 - 74 netreba) na začiatku SELECT z neho vybereiem

