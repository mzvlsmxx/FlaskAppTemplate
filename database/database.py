import os

import mysql.connector
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
passwd = os.getenv('DB_PASSWD')


def create_database() -> None:
    """
    Creates database named <database_name>

    :return: None
    """
    connection = mysql.connector.connect(host=host, user=user, passwd=passwd)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        CREATE DATABASE IF NOT EXISTS database_name;
        """
    )
    connection.commit()
    cursor.close()
    connection.close()


def create_table() -> None:
    """
    Creates table <table_name> in <database_name>

    :return: None
    """
    connection = mysql.connector.connect(host=host, user=user, passwd=passwd)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS database_name.table_name(
            id BIGINT NOT NULL AUTO_INCREMENT,
            PRIMARY KEY (id)
        );
        """
    )
    connection.commit()
    cursor.close()
    connection.close()


async def get_all_entries() -> dict[int, dict[str, int]]:
    """
    Select all entries from <database_name>.<table_name> table

    :return: Dict
    """
    connection = mysql.connector.connect(host=host, user=user, passwd=passwd)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        SELECT * FROM <database_name>.<table_name>;
        """
    )

    result = cursor.fetchall()

    connection.commit()
    cursor.close()
    connection.close()

    return {}
