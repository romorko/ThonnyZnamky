class Znamky:

    predmety = {"sj", "aj", "ma", "fy", "che", "bi"}
    hodnoty = {1, 2, 3, 4, 5}

    def __init__(
        self, nove_meno: str, nove_priezvisko: str, nove_znamky: dict[str, int]
    ):
        self.meno = nove_meno
        self.priezvisko = nove_priezvisko
        self.znamky = nove_znamky
    
    def __str__(self):
        return f'{self.meno} {self.priezvisko} {self.znamky}'
    
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

    #     @znamky.setter
    #     def znamky(self, other):
    #         if isinstance(other, dict):
    #             for key, value in other.items():
    #                 if not isinstance(key, str):
    #                     raise TypeError("Nazov predmetu musi byt text!")
    #                 if not isinstance(value, int):
    #                     raise TypeError("Znamka musi byt cislo!")
    #                 if not 1 <= value <= 5:
    #                     raise ValueError("Znamky su od 1 do 5")
    #             self._znamky = other.copy()
    #         else:
    #             raise TypeError("Znamky musia byt slovnik!")

    @znamky.setter
    def znamky(self, other):
        if isinstance(other, dict):
            for key, value in other.items():
                if key not in self.predmety:
                    raise ValueError(f"Nepovoleny nazov predmetu:<{key}> Mozne hodnoty:{self.predmety}")
                if value not in self.hodnoty:
                    raise ValueError("Znamka musi byt cislo od 1 do 5")
            self._znamky = other.copy()
        else:
            raise TypeError("Znamky musia byt slovnik!")


Z = Znamky("Roman", "Ravas", {"sj": 1, "aj": 1, "ma": 1, "fy": 1, "che": 1, "bi": 1})
print(Z)
