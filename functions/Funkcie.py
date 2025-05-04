from entities.Kniha import Kniha
from entities.Vypozicka import Vypozicka
from entities.Autor import Autor
from entities.Pouzivatel import Pouzivatel

def pridat_knihu(knihy, nazov, autor_id):
    nova_kniha = Kniha(len(knihy) + 1, nazov, autor_id)
    knihy.append(nova_kniha)
    return nova_kniha

from datetime import datetime

def vypozicat_knihu(knihy, vypozicky, kniha_id, pouzivatel_id):
    for kniha in knihy:
        if kniha.id == kniha_id and kniha.dostupna:
            kniha.vypozicat()
            nova_vypozicka = Vypozicka(len(vypozicky) + 1, kniha_id, pouzivatel_id,datetime.now())
            vypozicky.append(nova_vypozicka)
            return True
    return False

def vratit_knihu(knihy, vypozicky, vypozicka_id):
    for vypozicka in vypozicky:
        if vypozicka.id == vypozicka_id and vypozicka.datum_vratenia is None:
            vypozicka.vratit(datetime.now())
            for kniha in knihy:
                if kniha.id == vypozicka.kniha_id:
                    kniha.vratit()
                    return True
    return False

def ziskat_knihy_podla_autora(knihy, autori, meno_autora):
    for autor in autori:
        if autor.meno.lower() == meno_autora.lower():
            return [kniha.to_dict() for kniha in knihy if kniha.autor_id == autor.id]
    return None

def ziskat_historiu_vypoziciek_knihy(vypozicky, pouzivatelia, kniha_id):
    historia = []
    for vypozicka in vypozicky:
        if vypozicka.kniha_id == kniha_id:
            pouzivatel = next((p for p in pouzivatelia if p.id == vypozicka.pouzivatel_id), None)
            if pouzivatel:
                historia.append({
                    "meno": pouzivatel.meno,
                    "datum_vypozicky": vypozicka.datum_vypozicky.isoformat() if vypozicka.datum_vypozicky else None,
                    "datum_vratenia": vypozicka.datum_vratenia.isoformat() if vypozicka.datum_vratenia else None
                })
    return historia

