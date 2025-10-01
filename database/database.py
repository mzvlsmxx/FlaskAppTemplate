import os
import contextlib

import mysql.connector
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
passwd = os.getenv('DB_PASSWD')


def create_database() -> None:
    """
    Creates database

    :return: None
    """
    with contextlib.closing(mysql.connector.connect(host=host, user=user, passwd=passwd)) as connection:  # auto-closes connection
        with connection:  # auto-commits
            with contextlib.closing(connection.cursor()) as cursor:  # auto-closes cursor
                cursor.execute(
                    f"""
                    CREATE DATABASE IF NOT EXISTS database_name;
                    """
                )


def create_table() -> None:
    """
    Creates table

    :return: None
    """
    with contextlib.closing(mysql.connector.connect(host=host, user=user, passwd=passwd)) as connection:  # auto-closes connection
        with connection:  # auto-commits
            with contextlib.closing(connection.cursor()) as cursor:  # auto-closes cursor
                cursor.execute(
                    f"""
                    CREATE TABLE IF NOT EXISTS database_name.table_name(
                        id MEDIUMINT NOT NULL AUTO_INCREMENT,
                        PRIMARY KEY (id)
                    );
                    """
                )
