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


def pridaj_ziaka(ziak) -> int|None :
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
                ziak.hodnotenie
            ),
        )

        return cur.lastrowid


def najdi_ziaka(hladaj_priezvisko) -> list[tuple]:
    with otvor_databazu() as conn:
        cur = conn.execute(
            "SELECT * FROM ziaci WHERE priezvisko = ?", (hladaj_priezvisko.capitalize(),)
        )

        # return cur.lastrowid
        return cur.fetchall()


def vymaz_ziaka(vymaz_priezvisko) -> bool | int | None :
    najdene = najdi_ziaka(vymaz_priezvisko)
    if not najdene:
        return False
    else:
        for jeden in najdene:
            print(jeden)
        id = int(input("Zadaj ID ziaka na vymazanie"))
        with otvor_databazu() as conn:
            cur = conn.execute("DELETE FROM ziaci WHERE pc = ?", (id,))
        return cur.lastrowid


def vypis_zaznamy() -> list[tuple]:
    with otvor_databazu() as conn:
        cur = conn.execute("SELECT * FROM ziaci ORDER BY priezvisko")

        # return cur.lastrowid
        return cur.fetchall()
