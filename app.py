from flask import Flask, redirect
import os

from werkzeug.utils import secure_filename

from routes.auth_routes import auth_bp
from routes.dashboard_routes import dashboard_bp
from routes.medicine_routes import medicine_bp
from routes.history_routes import history_bp
from routes.notification_routes import notification_bp


app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.secret_key = "meditrack_secret"

# HOME ROUTE

@app.route('/')
def home():
    return redirect('/login')


# REGISTER BLUEPRINTS

app.register_blueprint(auth_bp, url_prefix="")
app.register_blueprint(dashboard_bp)
app.register_blueprint(medicine_bp)
app.register_blueprint(history_bp)
app.register_blueprint(notification_bp)


if __name__ == "__main__":
    app.run(debug=True)