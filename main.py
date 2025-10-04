if __name__ == '__main__':
    import os

    from dotenv import find_dotenv, load_dotenv

    from create import app
    from endpoints import endpoints
    from database import create_database, create_table

    endpoints.register_endpoints(app)

    create_database()
    create_table()

    load_dotenv(find_dotenv())

    app.run(
        host=os.getenv('APP_HOST'),  # type: ignore
        port=os.getenv('APP_PORT'),  # type: ignore
        debug=os.getenv('APP_DEBUG')  # type: ignore
    )
