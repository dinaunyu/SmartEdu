import sqlite3
import pandas as pd

# =========================
# KONEKSI DATABASE
# =========================
conn = sqlite3.connect(
    "nilai.db",
    check_same_thread=False
)

c = conn.cursor()

# =========================
# BUAT TABEL NILAI
# =========================
def create_table():

    c.execute("""
    CREATE TABLE IF NOT EXISTS nilai (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        tugas INTEGER,
        uts INTEGER,
        uas INTEGER,
        nilai_akhir REAL,
        grade TEXT,
        keterangan TEXT
    )
    """)

    conn.commit()

# =========================
# TAMBAH DATA
# =========================
def tambah_data(
    nama,
    tugas,
    uts,
    uas,
    nilai_akhir,
    grade,
    ket
):

    c.execute("""
    INSERT INTO nilai
    (
        nama,
        tugas,
        uts,
        uas,
        nilai_akhir,
        grade,
        keterangan
    )
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        nama,
        tugas,
        uts,
        uas,
        nilai_akhir,
        grade,
        ket
    ))

    conn.commit()

# =========================
# AMBIL DATA
# =========================
def ambil_data():

    return pd.read_sql(
        "SELECT * FROM nilai",
        conn
    )

# =========================
# UPDATE DATA
# =========================
def update_data(
    id,
    nama,
    tugas,
    uts,
    uas,
    nilai_akhir,
    grade,
    ket
):

    c.execute("""
    UPDATE nilai
    SET
        nama=?,
        tugas=?,
        uts=?,
        uas=?,
        nilai_akhir=?,
        grade=?,
        keterangan=?
    WHERE id=?
    """, (
        nama,
        tugas,
        uts,
        uas,
        nilai_akhir,
        grade,
        ket,
        id
    ))

    conn.commit()

# =========================
# HAPUS DATA
# =========================
def hapus_data(id):

    c.execute("""
    DELETE FROM nilai
    WHERE id=?
    """, (id,))

    conn.commit()

# =========================
# TABEL PROFIL
# =========================
def create_profile_table():

    c.execute("""
    CREATE TABLE IF NOT EXISTS profil (
        username TEXT PRIMARY KEY,
        nama TEXT,
        nim TEXT,
        semester TEXT,
        alamat TEXT
    )
    """)

    conn.commit()

# =========================
# SIMPAN PROFIL
# =========================
def simpan_profil(
    username,
    nama,
    nim,
    semester,
    alamat
):

    create_profile_table()

    c.execute("""
    INSERT OR REPLACE INTO profil
    (
        username,
        nama,
        nim,
        semester,
        alamat
    )
    VALUES (?, ?, ?, ?, ?)
    """, (
        username,
        nama,
        nim,
        semester,
        alamat
    ))

    conn.commit()

# =========================
# AMBIL PROFIL
# =========================
def ambil_profil(username):

    create_profile_table()

    c.execute("""
    SELECT *
    FROM profil
    WHERE username=?
    """, (username,))

    return c.fetchone()

# =========================
# AUTO CREATE TABLE
# =========================
create_table()
create_profile_table()