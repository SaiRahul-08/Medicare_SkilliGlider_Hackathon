from flask import render_template

alerts = [
    {
        "title": "Medicine Reminder",
        "message": "Time to take Dolo 650 at 8:00 AM"
    },

    {
        "title": "Low Stock Alert",
        "message": "Dolo 650 stock is running low."
    }
]

def notifications():

    return render_template(
        "notifications.html",
        alerts=alerts
    )