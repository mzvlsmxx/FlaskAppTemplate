if __name__ != '__main__':
    import os
    from pathlib import Path

    import mysql.connector
    from flask import Flask
    from flask_cors import CORS
    from dotenv import load_dotenv, find_dotenv

    app: Flask = Flask(__name__, template_folder=Path('./templates'))
    CORS(app)

    load_dotenv(find_dotenv())

    db = None
    try:
        db = mysql.connector.connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            passwd=os.getenv('DB_PASSWD')
        )
    except mysql.connector.errors.DatabaseError:
        print("\033[91m" + "Error: Database connection error" + "\033[0m")

