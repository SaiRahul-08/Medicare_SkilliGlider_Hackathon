from flask import render_template

history_data = []

def history():

    return render_template(
        "history.html",
        history_data=history_data
    )