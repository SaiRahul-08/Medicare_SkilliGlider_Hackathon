from flask import render_template, request, redirect, url_for, session, flash
from models.user_model import check_user_login, create_user


def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = check_user_login(email, password)

        if user:

            session["user"] = {
                "id": user["id"],
                "name": user["name"],
                "username": user["username"],
                "email": user["email"],
                "age": user["age"],
                "sex": user["sex"],
                "dob": user["dob"],
                "doctor": user["doctor"],
                "height": user["height"],
                "weight": user["weight"],
                "profile_pic": user["profile_pic"]
            }

            flash("Login Successful", "success")

            return redirect(url_for("dashboard.dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")


def signup():

    if request.method == "POST":

        name = request.form.get("name")
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")

        create_user(name, username, email, password)

        flash("Account Created Successfully", "success")

        return redirect(url_for("auth.login"))

    return render_template("signup.html")


def logout():

    session.clear()

    return redirect(url_for("auth.login"))