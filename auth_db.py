import sqlite3

# =========================
# KONEKSI DATABASE
# =========================
conn = sqlite3.connect(
    "user.db",
    check_same_thread=False
)

c = conn.cursor()

# =========================
# BUAT TABEL USER
# =========================
def create_user_table():

    c.execute("""
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        password TEXT,
        nim TEXT
    )
    """)

    conn.commit()

# =========================
# REGISTER USER
# =========================
def register_user(username, password, nim):

    if not username or not password or not nim:
        return "Semua field wajib diisi!"

    # cek username
    c.execute(
        "SELECT username FROM users WHERE username=?",
        (username,)
    )

    if c.fetchone():
        return "Username sudah digunakan!"

    # insert user
    c.execute("""
    INSERT INTO users
    (username, password, nim)
    VALUES (?, ?, ?)
    """, (username, password, nim))

    conn.commit()

    return "Registrasi berhasil!"

# =========================
# LOGIN USER
# =========================
def login_user(username, password):

    c.execute("""
    SELECT username, password, nim
    FROM users
    WHERE username=? AND password=?
    """, (username, password))

    return c.fetchone()

# =========================
# AMBIL USER
# =========================
def get_user(username):

    c.execute("""
    SELECT username, password, nim
    FROM users
    WHERE username=?
    """, (username,))

    return c.fetchone()

# =========================
# JALANKAN TABLE
# =========================
create_user_table()