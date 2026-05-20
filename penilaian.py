import streamlit as st
import base64
from auth_db import login_user, register_user, create_user_table
from nilai_db import *

# =========================
# INIT DATABASE
# =========================
create_user_table()
create_table()

# =========================
# CONFIG
# =========================
st.set_page_config(
    page_title="SmartEdu",
    layout="wide"
)

# =========================
# SESSION
# =========================
if "login" not in st.session_state:
    st.session_state.login = False

if "page" not in st.session_state:
    st.session_state.page = "landing"

# =========================
# STYLE
# =========================
st.markdown("""
<style>

/* BACKGROUND */
.stApp{
    background:
    radial-gradient(circle at top,#0f172a,#020617);
}

/* HIDE STREAMLIT */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* SIDEBAR */
section[data-testid="stSidebar"]{
    background: linear-gradient(
        180deg,
        #0047ff,
        #0094ff
    );
}

/* SIDEBAR TEXT */
section[data-testid="stSidebar"] *{
    color:white !important;
}

/* HERO */
.hero {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    text-align: center;

    margin-top: -35px;
    gap: 6px;
}
/* TITLE */
.title {
    font-size: 64px;   /* sebelumnya terlalu besar */
    font-weight: 800;

    white-space: nowrap;   /* 🔥 biar tidak turun */
    overflow: hidden;

    margin-top: 10px;
    margin-bottom: 15px;

    background: linear-gradient(
        90deg,
        #00d4ff,
        #00a2ff,
        #0072ff
    );

    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
/* SUBTITLE */
.subtitle{

    font-size:22px;
    color:#cbd5e1;

    margin-top:5px;
    margin-bottom:28px;
}

/* BUTTON */
.stButton > button{

    width:240px;
    height:60px;

    border:none;
    border-radius:18px;

    font-size:22px;
    font-weight:700;

    color:white;

    background: linear-gradient(
        90deg,
        #06b6d4,
        #2563eb
    );

    box-shadow:0 0 30px rgba(37,99,235,0.5);

    transition:0.3s;
}

/* INPUT */
.stTextInput input,
.stNumberInput input{

    background-color:rgba(255,255,255,0.08) !important;

    color:white !important;

    border-radius:14px !important;

    border:none !important;

    height:52px;
}

/* SELECTBOX */
.stSelectbox div[data-baseweb="select"]{

    background-color:rgba(0,0,0,0.3);

    border-radius:14px;
}

/* TEXT */
label,p,h1,h2,h3,h4,h5,h6{
    color:white !important;
}

/* DATAFRAME */
[data-testid="stDataFrame"]{
    border-radius:15px;
    overflow:hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOGO
# =========================
def tampilkan_logo(size=150):

    try:

        with open("SmartEdu.png","rb") as f:
            data = base64.b64encode(f.read()).decode()

        st.markdown(f"""
        <div style='text-align:center'>
            <img src='data:image/png;base64,{data}' width='{size}'>
        </div>
        """, unsafe_allow_html=True)

    except:
        pass

# =========================
# RULE BASED
# =========================
def hitung_nilai(tugas, uts, uas):

    nilai = (0.3*tugas) + (0.3*uts) + (0.4*uas)

    if nilai >= 85:
        return nilai,"A","Sangat Baik"

    elif nilai >= 75:
        return nilai,"B","Baik"

    elif nilai >= 65:
        return nilai,"C","Cukup"

    else:
        return nilai,"D","Kurang"

# =========================
# LANDING PAGE
# =========================
def landing_page():

    st.markdown("""
    <style>

    .block-container{
        padding-top:20px !important;
    }

    /* WRAPPER */
    .landing-wrapper{
        text-align:center;
        width:100%;
    }

    /* TITLE */
    .landing-title{

        text-align:center;

        font-size:72px;
        font-weight:900;

        margin-top:10px;
        margin-bottom:8px;

        background: linear-gradient(
            90deg,
            #00d4ff,
            #00a2ff,
            #0072ff
        );

        -webkit-background-clip:text;
        -webkit-text-fill-color:transparent;
    }

    /* SUBTITLE */
    .landing-subtitle{

        text-align:center;

        font-size:24px;
        color:#cbd5e1;

        margin-bottom:30px;
    }

    /* BUTTON */
    div.stButton > button{

        width:240px !important;
        height:58px !important;

        border:none !important;
        border-radius:16px !important;

        font-size:20px !important;
        font-weight:700 !important;

        color:white !important;

        background: linear-gradient(
            90deg,
            #06b6d4,
            #2563eb
        ) !important;

        display:block !important;
        margin:auto !important;
    }

    </style>
    """, unsafe_allow_html=True)

    # CENTER
    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown(
            "<div class='landing-wrapper'>",
            unsafe_allow_html=True
        )

        # LOGO CENTER
        logo1, logo2, logo3 = st.columns([1,2,1])

        with logo2:
            tampilkan_logo(170)

        # TITLE CENTER
        st.markdown("""
        <div class='landing-title'>
            SmartEdu
        </div>
        """, unsafe_allow_html=True)

        # SUBTITLE CENTER
        st.markdown("""
        <div class='landing-subtitle'>
            Sistem Penilaian Mahasiswa
        </div>
        """, unsafe_allow_html=True)

        # BUTTON CENTER
        b1, b2, b3 = st.columns([1,2,1])

        with b2:

            if st.button("Mulai"):

                st.session_state.page = "auth"
                st.rerun()

        st.markdown("</div>", unsafe_allow_html=True)
# =========================
# LOGIN PAGE
# =========================
def login_page():

    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        data = login_user(username,password)

        if data:

            st.session_state.login = True
            st.session_state.user = data[0]
            st.session_state.nim = data[2]

            st.rerun()

        else:
            st.error("Login gagal")

# =========================
# REGISTER PAGE
# =========================
def register_page():

    st.title("Register")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    nim = st.text_input("NIM")

    if st.button("Daftar"):

        hasil = register_user(
            username,
            password,
            nim
        )

        st.success(hasil)

# =========================
# ROUTING
# =========================
if not st.session_state.login:

    if st.session_state.page == "landing":

        landing_page()
        st.stop()

    menu_auth = st.sidebar.selectbox(
        "Menu",
        ["Login","Register"]
    )

    if menu_auth == "Login":
        login_page()

    else:
        register_page()

    st.stop()

# =========================
# SIDEBAR
# =========================
st.sidebar.success(
    f"👤 {st.session_state.user}"
)

if st.sidebar.button("Logout"):

    st.session_state.login = False
    st.session_state.page = "landing"

    st.rerun()

menu = st.sidebar.selectbox(
    "Menu",
    ["Profil","Tambah","Lihat","Edit","Hapus"]
)

# =========================
# PROFIL
# =========================
if menu == "Profil":

    st.title("Profil User")

    # DEFAULT SESSION
    if "nama_profil" not in st.session_state:
        st.session_state.nama_profil = st.session_state.user

    if "nim_profil" not in st.session_state:
        st.session_state.nim_profil = st.session_state.nim

    if "semester_profil" not in st.session_state:
        st.session_state.semester_profil = "4"

    if "alamat_profil" not in st.session_state:
        st.session_state.alamat_profil = "Semarang"

    # =========================
    # CARD PROFIL
    # =========================
    st.markdown(f"""
    <div style="
        background: rgba(255,255,255,0.06);
        padding:25px;
        border-radius:18px;
        margin-bottom:25px;
        border:1px solid rgba(255,255,255,0.08);
    ">

    <h2 style="color:white;">
        👤 {st.session_state.nama_profil}
    </h2>

    <p style="color:#cbd5e1;font-size:18px;">
        🆔 NIM : {st.session_state.nim_profil}
    </p>

    <p style="color:#cbd5e1;font-size:18px;">
        📚 Semester : {st.session_state.semester_profil}
    </p>

    <p style="color:#cbd5e1;font-size:18px;">
        📍 Alamat : {st.session_state.alamat_profil}
    </p>

    </div>
    """, unsafe_allow_html=True)

    # =========================
    # FORM EDIT
    # =========================
    st.subheader("Edit Profil")

    nama = st.text_input(
        "Nama",
        value=st.session_state.nama_profil
    )

    nim = st.text_input(
        "NIM",
        value=st.session_state.nim_profil
    )

    semester = st.text_input(
        "Semester",
        value=st.session_state.semester_profil
    )

    alamat = st.text_area(
        "Alamat",
        value=st.session_state.alamat_profil
    )

    # =========================
    # BUTTON SIMPAN
    # =========================
    if st.button("Simpan Profil"):

        st.session_state.nama_profil = nama
        st.session_state.nim_profil = nim
        st.session_state.semester_profil = semester
        st.session_state.alamat_profil = alamat

        st.success("Profil berhasil diupdate")

        st.rerun()
# =========================
# TAMBAH
# =========================
elif menu == "Tambah":

    st.title("Tambah Data")

    nama = st.text_input("Nama Mahasiswa")

    tugas = st.number_input(
        "Nilai Tugas",
        0,
        100
    )

    uts = st.number_input(
        "Nilai UTS",
        0,
        100
    )

    uas = st.number_input(
        "Nilai UAS",
        0,
        100
    )

    if st.button("Simpan"):

        nilai, grade, ket = hitung_nilai(
            tugas,
            uts,
            uas
        )

        tambah_data(
            nama,
            tugas,
            uts,
            uas,
            nilai,
            grade,
            ket
        )

        st.success("Data berhasil disimpan")

        st.metric(
            "Nilai Akhir",
            round(nilai,2)
        )

        st.write("Grade :", grade)
        st.write("Keterangan :", ket)

# =========================
# LIHAT
# =========================
elif menu == "Lihat":

    st.title("Data Mahasiswa")

    st.dataframe(
        ambil_data(),
        use_container_width=True
    )

# =========================
# EDIT
# =========================
elif menu == "Edit":

    st.title("Edit Data")

    data = ambil_data()

    st.dataframe(data)

    if not data.empty:

        id_edit = st.selectbox(
            "Pilih ID",
            data["id"]
        )

        row = data[data["id"] == id_edit]

        nama = st.text_input(
            "Nama",
            row.iloc[0]["nama"]
        )

        tugas = st.number_input(
            "Tugas",
            0,
            100,
            int(row.iloc[0]["tugas"])
        )

        uts = st.number_input(
            "UTS",
            0,
            100,
            int(row.iloc[0]["uts"])
        )

        uas = st.number_input(
            "UAS",
            0,
            100,
            int(row.iloc[0]["uas"])
        )

        if st.button("Update"):

            nilai, grade, ket = hitung_nilai(
                tugas,
                uts,
                uas
            )

            update_data(
                id_edit,
                nama,
                tugas,
                uts,
                uas,
                nilai,
                grade,
                ket
            )

            st.success("Data berhasil diupdate")

# =========================
# HAPUS
# =========================
elif menu == "Hapus":

    st.title("Hapus Data")

    data = ambil_data()

    st.dataframe(data)

    id_hapus = st.selectbox(
        "Pilih ID",
        data["id"]
    )

    if st.button("Hapus"):

        hapus_data(id_hapus)

        st.success("Data berhasil dihapus")