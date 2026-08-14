import sqlite3
from common.utils import get_int


class Ziak:

    predmety = ("sj", "aj", "ma", "fy", "che", "bi")
    predmety_kontrola = frozenset(predmety)
    hodnoty = {1, 2, 3, 4, 5}

    def __init__(
        self, nove_meno: str, nove_priezvisko: str, nove_znamky: dict[str, int]
    ):
        self.meno = nove_meno
        self.priezvisko = nove_priezvisko
        self.znamky = nove_znamky

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.znamky} {self.priemer:.2f} {self.hodnotenie}"

    @property
    def meno(self):
        return self._meno

    @meno.setter
    def meno(self, other):
        if isinstance(other, str):
            self._meno = other
        else:
            raise TypeError("Nespravny typ dat!")

    @property
    def priezvisko(self):
        return self._priezvisko

    @priezvisko.setter
    def priezvisko(self, other):
        if isinstance(other, str):
            self._priezvisko = other
        else:
            raise TypeError("Nespravny typ dat!")

    @property
    def znamky(self):
        return self._znamky

    @znamky.setter
    def znamky(self, other):
        if isinstance(other, dict):
            for key, value in other.items():
                if key not in self.predmety_kontrola:
                    raise ValueError(
                        f"Nepovoleny nazov predmetu:<{key}> Mozne hodnoty:{self.predmety_kontrola}"
                    )
                if value not in self.hodnoty:
                    raise ValueError("Znamka musi byt cislo od 1 do 5")
            self._znamky = other.copy()
        else:
            raise TypeError("Znamky musia byt slovnik!")

    @property
    def priemer(self) -> float:
        return sum(self._znamky.values()) / len(self._znamky)

    @property
    def hodnotenie(self) -> str:
        znamky = self._znamky.values()

        priemer = self.priemer
        najhorsia_znamka = max(znamky)

        if najhorsia_znamka == 5:
            return "neprospel"

        if priemer <= 1.5 and najhorsia_znamka <= 2:
            return "prospel s vyznamenaním"

        if priemer <= 2.0 and najhorsia_znamka <= 3:
            return "prospel veľmi dobre"

        return "prospel"


def nacitaj_znamky() -> Ziak:
    nacitaj_meno = input("Zadaj meno:")
    nacitaj_priezvisko = input("Zadaj priezvisko:")
    zapisat = {}
    for predmet in Ziak.predmety:
        text = f"Zadaj znamku z {predmet.upper()}:"
        zapisat[predmet] = get_int(text, 1, 5, False)
    return Ziak(nacitaj_meno, nacitaj_priezvisko, zapisat)


ziak = Ziak("Roman", "Ravas", {"sj": 1, "aj": 1, "ma": 1, "fy": 1, "che": 1, "bi": 1})
with sqlite3.connect("znamky.db") as conn:
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO ziaci (meno, priezvisko,sj,aj,ma,fy,che,bi,priemer,hodnotenie) VALUES (?,?,?,?,?,?,?,?,?,?)",
        (
            ziak.meno,
            ziak.priezvisko,
            ziak.znamky["sj"],
            ziak.znamky["aj"],
            ziak.znamky["ma"],
            ziak.znamky["fy"],
            ziak.znamky["che"],
            ziak.znamky["bi"],
            ziak.priemer,
            ziak.hodnotenie,
        ),
    )
    conn.commit()  # pri with nie je nutný, ale pri učení je názorný
    # cur.execute("SELECT * FROM ziaci")
    # print(cur.fetchall())


# Z = Ziak("Roman", "Ravas", {"sj": 1, "aj": 1, "ma": 1, "fy": 1, "che": 1, "bi": 1})
# Z1 = nacitaj_znamky()
