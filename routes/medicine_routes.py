from flask import Blueprint, render_template, request, redirect, session, flash
from database.db_connection import get_db_connection

medicine_bp = Blueprint('medicine_bp', __name__)


# =========================================
# ADD MEDICINE
# =========================================

@medicine_bp.route('/add-medicine', methods=['GET', 'POST'])
def add_medicine():

    if 'user' not in session:
        return redirect('/login')

    if 'history' not in session:
        session['history'] = []

    if request.method == 'POST':

        name = request.form.get('name')
        dosage = request.form.get('dosage')

        hour = request.form.get('hour')
        minute = request.form.get('minute')
        period = request.form.get('period')

        timing = f"{hour}:{minute} {period}"

        stock = request.form.get('stock')

        conn = get_db_connection()
        cursor = conn.cursor()

        # SQLITE USES ? NOT %s

        cursor.execute("""
            INSERT INTO medicines (name, dosage, timing, stock)
            VALUES (?, ?, ?, ?)
        """, (name, dosage, timing, stock))

        conn.commit()
        conn.close()

        # HISTORY

        history = session.get('history', [])
        history.append(f"Added medicine: {name}")
        session['history'] = history

        flash("Medicine added successfully", "success")

        return redirect('/medicine-list')

    return render_template('add_medicine.html')


# =========================================
# MEDICINE LIST
# =========================================

@medicine_bp.route('/medicine-list')
def medicine_list():

    if 'user' not in session:
        return redirect('/login')

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM medicines
    """)

    rows = cursor.fetchall()

    conn.close()

    medicines = []

    for row in rows:

        medicines.append({
            "id": row[0],
            "name": row[1],
            "dosage": row[2],
            "timing": row[3],
            "stock": row[4]
        })

    return render_template(
        'medicine_list.html',
        medicines=medicines
    )


# =========================================
# EDIT MEDICINE
# =========================================

@medicine_bp.route('/edit-medicine/<int:id>', methods=['GET', 'POST'])
def edit_medicine(id):

    if 'user' not in session:
        return redirect('/login')

    conn = get_db_connection()
    cursor = conn.cursor()

    # GET MEDICINE

    cursor.execute("""
        SELECT * FROM medicines
        WHERE id = ?
    """, (id,))

    row = cursor.fetchone()

    if not row:

        conn.close()

        flash("Medicine not found", "danger")

        return redirect('/medicine-list')

    medicine = {
        "id": row[0],
        "name": row[1],
        "dosage": row[2],
        "timing": row[3],
        "stock": row[4]
    }

    if request.method == 'POST':

        name = request.form.get('name')
        dosage = request.form.get('dosage')

        hour = request.form.get('hour')
        minute = request.form.get('minute')
        period = request.form.get('period')

        timing = f"{hour}:{minute} {period}"

        stock = request.form.get('stock')

        # UPDATE

        cursor.execute("""
            UPDATE medicines
            SET
                name = ?,
                dosage = ?,
                timing = ?,
                stock = ?
            WHERE id = ?
        """, (name, dosage, timing, stock, id))

        conn.commit()
        conn.close()

        # HISTORY

        history = session.get('history', [])
        history.append(f"Edited medicine: {name}")
        session['history'] = history

        flash("Medicine updated successfully", "success")

        return redirect('/medicine-list')

    conn.close()

    return render_template(
        'edit_medicine.html',
        medicine=medicine
    )


# =========================================
# DELETE MEDICINE
# =========================================

@medicine_bp.route('/delete-medicine/<int:id>')
def delete_medicine(id):

    if 'user' not in session:
        return redirect('/login')

    conn = get_db_connection()
    cursor = conn.cursor()

    # GET MEDICINE NAME

    cursor.execute("""
        SELECT name FROM medicines
        WHERE id = ?
    """, (id,))

    row = cursor.fetchone()

    deleted_name = ""

    if row:
        deleted_name = row[0]

    # DELETE MEDICINE

    cursor.execute("""
        DELETE FROM medicines
        WHERE id = ?
    """, (id,))

    conn.commit()
    conn.close()

    # HISTORY

    history = session.get('history', [])
    history.append(f"Deleted medicine: {deleted_name}")
    session['history'] = history

    flash("Medicine deleted successfully", "success")

    return redirect('/medicine-list')


# =========================================
# HISTORY PAGE
# =========================================

@medicine_bp.route('/history')
def history():

    history_data = session.get('history', [])

    return render_template(
        'history.html',
        history=history_data
    )


# =========================================
# CLEAR HISTORY
# =========================================

@medicine_bp.route('/clear-history')
def clear_history():

    session['history'] = []

    flash("History cleared successfully", "success")

    return redirect('/history')