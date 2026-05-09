from flask import render_template

medicines = [
    {
        "name": "Dolo 650",
        "dosage": "2",
        "timing": "8am",
        "stock": 4
    }
]

def dashboard():

    total_medicines = len(medicines)

    low_stock = 0

    for medicine in medicines:

        if medicine["stock"] < 5:
            low_stock += 1

    return render_template(
        "dashboard.html",
        medicines=medicines,
        total_medicines=total_medicines,
        low_stock=low_stock
    )