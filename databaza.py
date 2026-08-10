import sqlite3

DATABAZA = "ziaci.db"


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


def pridaj_ziaka(other: Ziak) -> None:
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
                ziak.znamky["priemer"],
                ziak.znamky["hodnotenie"],
            ),
        )

        return cur.lastrowid


def najdi_ziaka(other: Ziak) -> Ziak:
    pass


def vymaz_ziaka(other: Ziak) -> None:
    pass


def vypis_zaznamy() -> None:
    pass
