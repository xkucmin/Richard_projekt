class Kniha:
    def __init__(self, id, nazov, autor_id, dostupna=True):
        self.id = id
        self.nazov = nazov
        self.autor_id = autor_id
        self.dostupna = dostupna

    def vypozicat(self, conn, cur):
        if self.dostupna:
            self.dostupna = False

            cur.execute(
                "UPDATE knihy SET dostupna = FALSE WHERE id = %s",
                (self.id,)  # make sure self.id is set to the DB row ID
            )
            conn.commit()

            return True
        return False

    # def vypozicat(self):
    #     if self.dostupna:
    #         self.dostupna = False
    #         return True
    #     return False

    def vratit(self, conn, cur):
        self.dostupna = True
        print (self.dostupna)
        cur.execute(
            "UPDATE knihy SET dostupna = True WHERE id = %s",
            (self.id,)  # make sure self.id is set to the DB row ID
        )
        conn.commit()

# riadok 12-16 to iste miesto dostupna False = dostupna true, poslat conn a cur
    def to_dict(self):
        return {
            "id": self.id,
            "nazov": self.nazov,
            "autor_id": self.autor_id,
            "dostupna": self.dostupna
        }