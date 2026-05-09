CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    username TEXT,
    email TEXT,
    password TEXT,
    age INTEGER,
    sex TEXT,
    dob TEXT,
    doctor TEXT,
    height TEXT,
    weight TEXT,
    profile_pic TEXT
);

CREATE TABLE IF NOT EXISTS medicines (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    medicine_name TEXT NOT NULL,
    dosage TEXT NOT NULL,
    timing TEXT NOT NULL,
    stock INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS family_profiles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    relation TEXT NOT NULL,
    age INTEGER,
    sex TEXT,
    blood_group TEXT,
    health_condition TEXT
);
