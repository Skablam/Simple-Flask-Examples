from flask import Flask
from .home.views import home
from .admin.views import admin
import os

app = Flask(__name__)

app.config.from_object(os.environ.get('SETTINGS'))
app.register_blueprint(home, url_prefix='/home')
app.register_blueprint(admin, url_prefix='/admin')

@app.route("/health")
def check_status():
    return "Status OK"
