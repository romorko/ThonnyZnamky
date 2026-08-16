import databaza
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


def vytvor_menu_uprav(upravujem_id: int) -> int | None:
    while (
        vyber := input(
            "Vyber jednu z moznosti\na - priezvisko\nb - meno\nc - Sj\nd - Aj\ne - Ma\nf - Fy\ng - Bi\nh - Che\nk - koniec\nZadaj volbu:"
        )
    ) != "k":
        match vyber:
            case "a":
                upravovane_pole = "Priezvisko"
            case "b":
                upravovane_pole = "Meno"
            case "c":
                upravovane_pole = "Sj"
            case "d":
                upravovane_pole = "Aj"
            case "e":
                upravovane_pole = "Ma"
            case "f":
                upravovane_pole = "Fy"
            case "g":
                upravovane_pole = "Bi"
            case "h":
                upravovane_pole = "Che"
            case "k":
                break
            case _:
                print("Neplatna volba")
        nova_hodnota:int|str        
        if vyber in ("a", "b"):
            nova_hodnota = input(f"Zadaj novu hodnotu pola {upravovane_pole.upper()}:")
        else:
            nova_hodnota = get_int(
                f"Zadaj znamku zo {upravovane_pole.upper()}:", 1, 5, False
            )

    return databaza.uprav_ziaka(upravovane_pole, upravujem_id, nova_hodnota)


def vytvor_menu() -> None:
    while (
        (
            vybrane := input(
                """***********************\nVyber jednu z moznosti:\n1 - vypis ziakov\n2 - pridaj ziaka\n3 - vymaz ziaka\n4 - najdi ziaka
5 - uprav ziaka\n6 - prepocitaj priemery\n7 - urob vyhodnotenie\nk - koniec\nZadaj volbu:"""
            )
        )
        != "k"
    ):
        match vybrane:
            case "1":
                vysledok = databaza.vypis_zaznamy()
                for zaznam in vysledok:
                    print(zaznam)
            case "2":
                databaza.pridaj_ziaka(nacitaj_znamky())
                print("Ziak bol pridany!")
            case "3":
                zmazat_id: int = get_int(
                    "Zadaj id ziaka, ktorého chceš vymazať:", 1, 1000, False
                )
                pocet_zmazanych = databaza.vymaz_ziaka(zmazat_id)
                if pocet_zmazanych == 0:
                    print(f"Ziak s ID {zmazat_id} sa nenasiel!")
                else:
                    print(f"Ziak s ID {zmazat_id} bol vymazany!")
            case "4":
                najst = input("Zadaj priezvisko hladaneho ziaka:")
                nasiel = databaza.najdi_ziaka(najst)
                if not nasiel:
                    print("Taky ziak tam nie je")
                else:
                    print(nasiel)
            case "5":
                upravit_id: int = get_int(
                    "Zadaj id ziaka, ktorého chceš upravit:", 1, 1000, False
                )
                pocet_upravenych = vytvor_menu_uprav(upravit_id)
                if pocet_upravenych is None:
                    print("Neplatna polozka menu!")
                elif pocet_upravenych == 0:
                    print("Ziak so zadanym ID sa nenasiel!")
                else:
                    print("Udaje ziaka boli zmenene!")
            case "6":
                prepocitane = databaza.prepocitaj_priemery()
                if prepocitane is not None:
                    print("Priemery boli prepocitane!")
            case "7":
                databaza.urob_vyhodnotenie()
            case "k":
                break
            case _:
                print("Neznama moznost")


# Z = Ziak("Roman", "Ravas", {"sj": 1, "aj": 1, "ma": 1, "fy": 1, "che": 1, "bi": 1})
# Z1 = nacitaj_znamky()
vytvor_menu()
