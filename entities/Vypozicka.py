class Vypozicka:
    def __init__(self, id, kniha_id, pouzivatel_id, datum_vypozicky, datum_vratenia=None):
        self.id = id
        self.kniha_id = kniha_id
        self.pouzivatel_id = pouzivatel_id
        self.datum_vypozicky = datum_vypozicky
        self.datum_vratenia = datum_vratenia

    def vratit(self, datum_vratenia, conn, cur):
        self.datum_vratenia = datum_vratenia

        cur.execute(
            "UPDATE vypozicky SET datum_vratenia = %s WHERE id = %s",
            (datum_vratenia, self.id,)  # make sure self.id is set to the DB row ID
        )
        conn.commit()

    def to_dict2(self):
        return {
            "id": self.id,
            "kniha_id": self.kniha_id,
            "pouzivatel_id": self.pouzivatel_id,
            "datum_vypozicky": self.datum_vypozicky.isoformat() if self.datum_vypozicky else None,
            "datum_vratenia": self.datum_vratenia.isoformat() if self.datum_vratenia else None
            }
