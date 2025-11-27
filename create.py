if __name__ != '__main__':
    from pathlib import Path

    from flask import Flask
    from flask_cors import CORS

    app: Flask = Flask(__name__, template_folder=Path('./templates'))
    CORS(app)
