from create import app
from endpoints import endpoints
from database import create_database, create_table

if __name__ == '__main__':
    endpoints.register_endpoints(app)

    create_database()
    create_table()

    app.run(
        host='0.0.0.0',
        port=7777,
        debug=True
    )
