from flask import Flask
from app.views.views import main_bp

app = Flask(__name__)

app.register_blueprint(main_bp)
