from database.db_connection import get_db_connection


# =========================================
# CREATE USER
# =========================================

def create_user(name, username, email, password):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO users (
            name,
            username,
            email,
            password
        )
        VALUES (?, ?, ?, ?)
    """, (name, username, email, password))

    conn.commit()

    conn.close()


# =========================================
# LOGIN USER (USERNAME ONLY)
# =========================================

def check_user_login(username, password):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE username = ?
        AND password = ?
    """, (username, password))

    user = cursor.fetchone()

    conn.close()

    if user:

        return {
            "id": user[0],
            "name": user[1],
            "username": user[2],
            "email": user[3],
            "password": user[4],
            "age": user[5] if len(user) > 5 else "",
            "sex": user[6] if len(user) > 6 else "",
            "dob": user[7] if len(user) > 7 else "",
            "doctor": user[8] if len(user) > 8 else "",
            "height": user[9] if len(user) > 9 else "",
            "weight": user[10] if len(user) > 10 else "",
            "profile_pic": user[11] if len(user) > 11 else ""
        }

    return None


# =========================================
# GET USER BY ID
# =========================================

def get_user_by_id(user_id):

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE id = ?
    """, (user_id,))

    user = cursor.fetchone()

    conn.close()

    if user:

        return {
            "id": user[0],
            "name": user[1],
            "username": user[2],
            "email": user[3],
            "password": user[4],
            "age": user[5] if len(user) > 5 else "",
            "sex": user[6] if len(user) > 6 else "",
            "dob": user[7] if len(user) > 7 else "",
            "doctor": user[8] if len(user) > 8 else "",
            "height": user[9] if len(user) > 9 else "",
            "weight": user[10] if len(user) > 10 else "",
            "profile_pic": user[11] if len(user) > 11 else ""
        }

    return None