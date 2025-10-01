from create import app, db
from endpoints import endpoints


if __name__ == '__main__':

    endpoints.register_endpoints(app)

    # CREATE ALL DATABASES, TABLES AND OTHER STRUCTURE
    # db.cursor().execute(
    #     """
    #     CREATE DATABASE IF NOT EXISTS database_name
    #     """
    # )
    # db.cursor().execute(
    #     """
    #     CREATE TABLE IF NOT EXISTS database_name.table_name
    #     """
    # )



    app.run(
        host='0.0.0.0',
        port=7777,
        debug=True
    )
