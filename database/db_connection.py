import sqlite3


def get_db_connection():

    conn = sqlite3.connect("database.db")

    conn.row_factory = sqlite3.Row

    return conn


def create_tables():

    conn = get_db_connection()

    cursor = conn.cursor()

    # USERS TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        username TEXT UNIQUE,
        email TEXT,
        password TEXT,

        age TEXT,
        sex TEXT,
        dob TEXT,
        doctor TEXT,
        height TEXT,
        weight TEXT,

        profile_pic TEXT
    )
    """)

    # MEDICINES TABLE
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicines (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        dosage TEXT,
        timing TEXT,
        stock INTEGER
    )
    """)

    conn.commit()

    conn.close()


create_tables()