class Kniha:
    def __init__(self, id, nazov, autor_id, dostupna=True):
        self.id = id
        self.nazov = nazov
        self.autor_id = autor_id
        self.dostupna = dostupna

    def vypozicat(self):
        if self.dostupna:
            self.dostupna = False
            return True
        return False

    def vratit(self):
        self.dostupna = True

    def to_dict(self):
        return {
            "id": self.id,
            "nazov": self.nazov,
            "autor_id": self.autor_id,
            "dostupna": self.dostupna
        }