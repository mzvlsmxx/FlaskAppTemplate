import os

import mysql.connector
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


host = os.getenv('DB_HOST')
user = os.getenv('DB_USER')
passwd = os.getenv('DB_PASSWD')


def create_database(database_name: str = 'database_name') -> None:
    """
    Creates database named <database_name>

    :return: None
    """
    connection = mysql.connector.connect(host=host, user=user, passwd=passwd)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        CREATE DATABASE IF NOT EXISTS {database_name};
        """
    )
    connection.commit()
    cursor.close()
    connection.close()


def create_table(database_name: str = 'database_name', table_name: str = 'table_name') -> None:
    """
    Creates table <table_name> in <database_name>

    :return: None
    """
    connection = mysql.connector.connect(host=host, user=user, passwd=passwd)
    cursor = connection.cursor()
    cursor.execute(
        f"""
        CREATE TABLE IF NOT EXISTS {database_name}.{table_name} (
            `id` INT NOT NULL UNIQUE AUTO_INCREMENT,
            `field_1` VARCHAR(90) NOT NULL,
            `field_2` TINYINT(1) NOT NULL DEFAULT 0,
            PRIMARY KEY (`task_id`)
            ) ENGINE = InnoDB;
        """
    )
    connection.commit()
    cursor.close()
    connection.close()


async def get_entries(
        id: int | None = None,
        field_1: int | str | None = None,
        field_2: int | str | None = None
) -> dict[int, dict[str, int]]:
    """
    Select entries from <database_name>.<table_name> table

    :param id: Select entry specified id
    :param field_1: Select task with specified field_1
    :param field_2: Select task with specified field_2
    :return: Dict like {<id>: {field_1: <field_1>, field_2: <field_2>}}
    """
    connection = mysql.connector.connect(host=host, user=user, passwd=passwd)
    cursor = connection.cursor()

    query: str = 'SELECT * FROM database_name.table_name'
    additional_criteria: bool = False
    
    if any(field != None for field in [id, field_1, field_2]):
        additional_criteria = True
        query += ' WHERE '

    if id != None:
        query += f'id = {id} AND '
    if field_1 != None:
        query += f'field_1 = "{field_1}" AND '
    if field_2 != None:
        query += f'field_2 = "{field_2}" AND '

    if additional_criteria:
        cursor.execute(query[:-5] + ';')
    else:
        cursor.execute(query + ';')

    result = {}

    for entry in cursor.fetchall():
        result.update(
            {
                entry[0]: {  # type: ignore
                    'field_1': entry[1],  # type: ignore
                    'field_2': entry[2]  # type: ignore
                }
            }
        )

    connection.commit()
    cursor.close()
    connection.close()

    return result
