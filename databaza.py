import sqlite3

DATABAZA = "znamky.db"


def otvor_databazu() -> sqlite3.Connection:
    return sqlite3.connect(DATABAZA)


def vytvor_tabulku() -> None:
    with otvor_databazu() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS ziaci (
                id INTEGER PRIMARY KEY,
                meno TEXT NOT NULL,
                priezvisko TEXT NOT NULL,
                sj INTEGER,
                aj INTEGER,
                ma INTEGER,
                fy INTEGER,
                che INTEGER,
                bi INTEGER,
                priemer DOUBLE,
                hodnotenie TEXT NOT NULL
            )
        """)


def pridaj_ziaka(ziak) -> int | None:
    with otvor_databazu() as conn:
        cur = conn.execute(
            """
            INSERT INTO ziaci (meno, priezvisko, sj, aj, ma, fy, che, bi,priemer,hodnotenie)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
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
        vlozene_id = cur.lastrowid
    return vlozene_id

def vypis_zaznamy() -> list[tuple]:
    with otvor_databazu() as conn:
        vypis_vysledok = conn.execute("SELECT * FROM ziaci ORDER BY priezvisko").fetchall()
    return vypis_vysledok

def najdi_ziaka(hladaj_priezvisko) -> list[tuple]:
    with otvor_databazu() as conn:
        najdene = conn.execute(
            "SELECT * FROM ziaci WHERE priezvisko = COLLATE NOCASE ?",  #ignoruje velkost pismen
            (hladaj_priezvisko.strip(),), #odstrani medzery pred a za
        ).fetchall()
    return najdene

def vymaz_ziaka(vymaz_priezvisko) -> int | None:
    hladaj_zmazat = najdi_ziaka(vymaz_priezvisko)
    if not hladaj_zmazat:
        return None
    else:
        for jeden in hladaj_zmazat:
            print(jeden)
        id = int(input("Zadaj ID ziaka na vymazanie:"))
        with otvor_databazu() as conn:
            cur = conn.execute("DELETE FROM ziaci WHERE id = ?", (id,))
            vymazane = cur.rowcount
        return vymazane


def uprav_ziaka(polozka_menu: str) -> int | None:
    match polozka_menu:
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
        case _:
            print("Neplatna volba")
            return None
    hladany_ziak = int(input("Zadaj ID ziaka, ktoreho udaj chces upravit:"))
    nova_hodnota = input(f"Zadaj novu hodnotu pola {upravovane_pole.upper()}:")
    with otvor_databazu() as conn:
        cur = conn.execute(
            f"UPDATE ziaci  SET {upravovane_pole} = ? WHERE id = ?",
            (nova_hodnota, hladany_ziak),
        )
        upravene_zaznamy = cur.rowcount
    prepocitaj_priemery(hladany_ziak)
    return upravene_zaznamy


def prepocitaj_priemery(id_ziaka: int | None = None) -> int | None:
    with otvor_databazu() as conn:
        if id_ziaka is None:
            cur = conn.execute("UPDATE ziaci  SET priemer = (Sj+Aj+Ma+Fy+Bi+Che)/6")
        else:
            cur = conn.execute(
                "UPDATE ziaci  SET priemer = (Sj+Aj+Ma+Fy+Bi+Che)/6 WHERE id =?",
                (id_ziaka,),
            )
        prepocitane = cur.rowcount
    return prepocitane


def urob_vyhodnotenie(id_ziaka: int | None = None) -> int|None:
    with otvor_databazu() as conn:
        if id_ziaka is None:
            cur = conn.execute("""UPDATE ziaci
                                    SET hodnotenie = CASE
                                                        WHEN max(sj,aj,ma,fy,che,bi)==5 THEN 'neprospel'
                                                        WHEN max(sj,aj,ma,fy,che,bi)<=2 and priemer <=1.5 THEN 'prospel s vyznamenanim'
                                                        WHEN max(sj,aj,ma,fy,che,bi)<=2 and priemer <=2.0 THEN 'prospel velmi dobre'
                                                        ELSE 'prospel'
                                                      END""")
        else:
            cur = conn.execute("""UPDATE ziaci
                                    SET hodnotenie = CASE
                                                        WHEN max(sj,aj,ma,fy,che,bi)==5 THEN 'neprospel'
                                                        WHEN max(sj,aj,ma,fy,che,bi)<=2 and priemer <=1.5 THEN 'prospel s vyznamenanim'
                                                        WHEN max(sj,aj,ma,fy,che,bi)<=2 and priemer <=2.0 THEN 'prospel velmi dobre'
                                                        ELSE 'prospel'
                                                      END WHERE id=?""",(id_ziaka,))
        pocet_zmien = cur.rowcount
    return pocet_zmien