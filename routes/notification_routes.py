from flask import Blueprint, render_template, session, redirect, request, current_app
from database.db_connection import get_db_connection
from werkzeug.utils import secure_filename
import os
import time

notification_bp = Blueprint('notification', __name__)


# =========================================
# NOTIFICATIONS
# =========================================

@notification_bp.route("/notifications")
def notifications():

    medicines = session.get('medicines', [])

    alerts = []

    for medicine in medicines:

        alerts.append({
            "title": "Medicine Reminder",
            "message": f"Time to take {medicine['name']} at {medicine['timing']} {medicine.get('period', '')}"
        })

        try:
            if int(medicine['stock']) <= 5:

                alerts.append({
                    "title": "Low Stock Alert",
                    "message": f"{medicine['name']} stock is running low."
                })

        except:
            pass

    return render_template(
        "notifications.html",
        alerts=alerts
    )


# =========================================
# PROFILE PAGE
# =========================================

@notification_bp.route("/profile")
def profile():

    if "user" not in session:
        return redirect("/login")

    user = session["user"]

    # DATABASE
    conn = get_db_connection()

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medicines")

    medicines = cursor.fetchall()

    conn.close()

    # TOTAL MEDICINES
    total_medicines = len(medicines)

    # BMI
    bmi = None
    bmi_status = "Not Available"

    try:

        height_cm = float(user.get("height", 0))
        weight_kg = float(user.get("weight", 0))

        if height_cm > 0 and weight_kg > 0:

            height_m = height_cm / 100

            bmi = round(weight_kg / (height_m * height_m), 1)

            if bmi < 18.5:
                bmi_status = "Underweight"

            elif bmi < 25:
                bmi_status = "Normal"

            elif bmi < 30:
                bmi_status = "Overweight"

            else:
                bmi_status = "Obese"

    except:
        pass

    return render_template(
        "profile.html",
        user=user,
        total_medicines=total_medicines,
        bmi=bmi,
        bmi_status=bmi_status
    )
# =========================================
# EDIT PROFILE
# =========================================

@notification_bp.route('/edit-profile', methods=['GET', 'POST'])
def edit_profile():

    if 'user' not in session:
        return redirect('/login')

    user = session.get('user')

    if request.method == 'POST':

        # =========================
        # TEXT FIELDS
        # =========================

        user['name'] = request.form.get('name')
        user['username'] = request.form.get('username')
        user['email'] = request.form.get('email')
        user['age'] = request.form.get('age')
        user['sex'] = request.form.get('sex')
        user['dob'] = request.form.get('dob')
        user['doctor'] = request.form.get('doctor')
        user['height'] = request.form.get('height')
        user['weight'] = request.form.get('weight')

        # =========================
        # PROFILE IMAGE
        # =========================

        profile_file = request.files.get('profile_pic')

        if profile_file and profile_file.filename != '':

            filename = f"{int(time.time())}_{secure_filename(profile_file.filename)}"

            upload_folder = os.path.join(
                current_app.root_path,
                'static',
                'uploads',
                'profile_pics'
            )

            # CREATE FOLDER
            os.makedirs(upload_folder, exist_ok=True)

            # FILE PATH
            file_path = os.path.join(upload_folder, filename)

            # SAVE IMAGE
            profile_file.save(file_path)

            # SAVE IMAGE PATH
            user['profile_pic'] = f"uploads/profile_pics/{filename}"

        # =========================
        # SAVE SESSION
        # =========================

        session['user'] = user
        session.modified = True

        return redirect('/profile')

    return render_template(
        'edit_profile.html',
        user=user
    )


# =========================================
# SETTINGS
# =========================================

@notification_bp.route("/settings")
def settings():

    return render_template("settings.html")