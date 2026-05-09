from flask import Blueprint, render_template, request, redirect, session, flash, url_for

from models.user_model import create_user, check_user_login

auth_bp = Blueprint('auth', __name__)


# =========================================
# SIGNUP
# =========================================

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():

    if request.method == 'POST':

        name = request.form.get('name')
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        try:

            create_user(
                name,
                username,
                email,
                password
            )

            flash("Signup Successful. Please Login.", "success")

            return redirect(url_for('auth.login'))

        except Exception as e:

            print(e)

            flash("Signup Failed", "danger")

            return redirect(url_for('auth.signup'))

    return render_template('signup.html')

# =========================
# LOGIN
# =========================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = check_user_login(username, password)

        print("USER FOUND:", user)

        if user:

            session["user"] = user

            flash("Login Successful", "success")

            return redirect(url_for("dashboard_bp.dashboard"))

        flash("Invalid Username or Password", "danger")

    return render_template("login.html")

# =========================================
# LOGOUT
# =========================================

@auth_bp.route('/logout')
def logout():

    session.clear()

    flash("Logged Out Successfully", "success")

    return redirect(url_for('auth.login'))