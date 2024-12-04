# app/app.py
from flask import Flask
from app.dash_app import create_dashboard

def create_app():
    app = Flask(__name__)
    create_dashboard(app)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
