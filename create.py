if __name__ != '__main__':
    import os
    from pathlib import Path

    from flask import Flask
    from flask_cors import CORS
    import mysql.connector 
    from dotenv import load_dotenv, find_dotenv

    app: Flask = Flask(__name__, template_folder=Path('./templates'))
    CORS(app)

    load_dotenv(find_dotenv())

    db = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        passwd=os.getenv('DB_PASSWD')
    )

