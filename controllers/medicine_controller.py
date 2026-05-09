from flask import render_template
from flask import request
from flask import redirect
from flask import url_for

medicines = []

def add_medicine():

    if request.method == "POST":

        name = request.form.get("name")
        dosage = request.form.get("dosage")
        timing = request.form.get("timing")
        stock = request.form.get("stock")

        medicine = {
            "name": name,
            "dosage": dosage,
            "timing": timing,
            "stock": int(stock)
        }

        medicines.append(medicine)

        return redirect(url_for("medicine_list"))

    return render_template("add_medicine.html")


def medicine_list():

    return render_template(
        "medicine_list.html",
        medicines=medicines
    )


def delete_medicine(index):

    if len(medicines) > index:

        medicines.pop(index)

    return redirect(url_for("medicine_list"))