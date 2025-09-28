from create import app, db
from endpoints import endpoints


if __name__ == '__main__':

    endpoints.register_endpoints(app)

    # db.cursor().execute(
    #     """
    #     CREATE DATABASE IF NOT EXISTS TestDatabase
    #     """
    # )

    app.run(
        host='0.0.0.0',
        port=7777,
        debug=True
    )
