from flask import Blueprint, render_template, session, redirect
from database.db_connection import get_db_connection
from datetime import datetime

dashboard_bp = Blueprint('dashboard_bp', __name__)


@dashboard_bp.route('/')
def home():

    return redirect('/login')


@dashboard_bp.route('/dashboard')
def dashboard():

    if 'user' not in session:
        return redirect('/login')

    # =========================================
    # WATER TRACKER RESET EVERY DAY
    # =========================================

    today_date = datetime.now().strftime("%Y-%m-%d")

    # FIRST TIME
    if 'water_date' not in session:

        session['water_date'] = today_date
        session['water_count'] = 0

    # NEW DAY RESET
    elif session['water_date'] != today_date:

        session['water_date'] = today_date
        session['water_count'] = 0

    water_count = session.get('water_count', 0)

    # =========================================
    # MEDICINE DATA
    # =========================================

    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicines")

    medicines = cursor.fetchall()

    conn.close()

    total_medicines = len(medicines)

    low_stock = 0

    for medicine in medicines:

        try:
            if int(medicine["stock"]) <= 5:
                low_stock += 1
        except:
            pass

    return render_template(
        'dashboard.html',
        total_medicines=total_medicines,
        low_stock=low_stock,
        water_count=water_count
    )


@dashboard_bp.route('/drink-water')
def drink_water():

    if 'water_count' not in session:
        session['water_count'] = 0

    if session['water_count'] < 8:
        session['water_count'] += 1

    return redirect('/dashboard')