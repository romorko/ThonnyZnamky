from random import uniform


def get_number(
    popis: str = "Zadaj číslo:",
    najmenej: float = -100.0,
    najviac: float = 100.0,
    nulaPovolena: bool = True,
) -> float:
    """Získava od uživateľa vstupnú hodnotu - reálne číslo zo zadaného intervalu a obmedzením nuly.

    Parametre:
        popis(str): textový reťazec, ktorý sa zobrazí uživateľovi
        najmenej(float): najmenšia možná zadaná hodnota
        najviac(float): najväčšia možná zadaná hodnota
        nulaPovolena(bool): či je možné zadať nulu (True/False)
    Návratová hodnota:
        cislo(float): uživateľom zadané číslo spĺňajúce podmienky
    Výnimky:
        ValueError: ak sa zadaný vstup nedá previesť na číslo
        ArithmeticError: ak zadaná hodnota nie je z požadovaného intervalu
        ZeroDivisionError: ak bola zadaná nula, ale nebola povolená
    """
    while True:
        try:
            cislo: float = float(
                input(
                    f"{popis} ∊ <{najmenej};{najviac}> nula je {'povolená' if nulaPovolena else 'zakázaná'}"
                    + ":"
                )
            )
        except ValueError:
            print("Zadaná hodnota nie je číslo!")
            continue

        if not najmenej <= cislo <= najviac:
            print("Zadaná hodnota nie je z intervalu!")
            continue

        if not nulaPovolena and cislo == 0.0:
            print("Nula nie je povolená!")
            continue

        return cislo

def get_int(
    popis: str = "Zadaj číslo:",
    najmenej: float = -100,
    najviac: float = 100,
    nulaPovolena: bool = True,
) -> int:
    """Získava od uživateľa vstupnú hodnotu - celé číslo zo zadaného intervalu a obmedzením nuly.

    Parametre:
        popis(str): textový reťazec, ktorý sa zobrazí uživateľovi
        najmenej(float): najmenšia možná zadaná hodnota
        najviac(float): najväčšia možná zadaná hodnota
        nulaPovolena(bool): či je možné zadať nulu (True/False)
    Návratová hodnota:
        cislo(float): uživateľom zadané číslo spĺňajúce podmienky
    Výnimky:
        ValueError: ak sa zadaný vstup nedá previesť na číslo
        ArithmeticError: ak zadaná hodnota nie je z požadovaného intervalu
        ZeroDivisionError: ak bola zadaná nula, ale nebola povolená
    """
    while True:
        try:
            cislo: int = int(
                input(
                    f"{popis} od {najmenej} do {najviac}, nula je {'povolená' if nulaPovolena else 'zakázaná'}"
                    + ":"
                )
            )
        except ValueError:
            print("Zadaná hodnota nie je číslo!")
            continue

        if not najmenej <= cislo <= najviac:
            print("Zadaná hodnota nie je celé číslo z povoleného rozsahu!")
            continue

        if not nulaPovolena and cislo == 0.0:
            print("Nula nie je povolená!")
            continue

        return cislo


def generuj_koeficient(najmensi: int = -100, najvacsi: int = 100) -> float:
    """Vygeneruje nahodné číslo z daného rozsahu.

    Parametre:
        najmensi(int): minimalna generovana hodnota
        najvacsi(int): maximalna generovana hodnota
    Návratová hodnota:
        vygenerované float číslo z daného intervalu
    """
    return round(uniform(najmensi, najvacsi), 2)
