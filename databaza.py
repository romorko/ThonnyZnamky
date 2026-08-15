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

        return cur.lastrowid


def najdi_ziaka(hladaj_priezvisko) -> list[tuple]:
    with otvor_databazu() as conn:
        cur = conn.execute(
            "SELECT * FROM ziaci WHERE priezvisko = ?",
            (hladaj_priezvisko.capitalize(),),
        )

        # return cur.lastrowid
        return cur.fetchall()


def vymaz_ziaka(vymaz_priezvisko) -> int | None:
    najdene = najdi_ziaka(vymaz_priezvisko)
    if not najdene:
        return None
    else:
        for jeden in najdene:
            print(jeden)
        id = int(input("Zadaj ID ziaka na vymazanie:"))
        with otvor_databazu() as conn:
            cur = conn.execute("DELETE FROM ziaci WHERE id = ?", (id,))
            return cur.rowcount


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
    hladany_ziak = input("Zadaj ID ziaka, ktoreho udaj chces upravit:")
    nova_hodnota = input(f"Zadaj novu hodnotu pola {upravovane_pole.upper()}:")
    with otvor_databazu() as conn:
        cur = conn.execute(
            f"UPDATE ziaci  SET {upravovane_pole} = ? WHERE id = ?",
            (nova_hodnota, hladany_ziak),
        )
        return cur.rowcount


def prepocitaj_priemery() -> int | None:
    with otvor_databazu() as conn:
        cur = conn.execute(f"UPDATE ziaci  SET priemer = (Sj+Aj+Ma+Fy+Bi+Che)/6")
        return cur.rowcount


def urob_vyhodnotenie() -> None:
    with otvor_databazu() as conn:
        cur = conn.execute("""UPDATE ziaci
                                SET hodnotenie = CASE
                                                    WHEN max(sj,aj,ma,fy,che,bi)==5 THEN 'neprospel'
                                                    WHEN max(sj,aj,ma,fy,che,bi)<=2 and priemer <=1.5 THEN 'prospel s vyznamenanim'
                                                    WHEN max(sj,aj,ma,fy,che,bi)<=2 and priemer <=2.0 THEN 'prospel velmi dobre'
                                                    ELSE 'prospel'
                                                  END""")
        return cur.rowcount


def vypis_zaznamy() -> list[tuple]:
    with otvor_databazu() as conn:
        cur = conn.execute("SELECT * FROM ziaci ORDER BY priezvisko")
        # return cur.lastrowid
        return cur.fetchall()
