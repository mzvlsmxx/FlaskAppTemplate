if __name__ == '__main__':
    import os

    from dotenv import find_dotenv, load_dotenv

    from create import app
    from endpoints import register_endpoints
    from exceptions import DatabaseConnectionError
    from utils import ensure_mysql_connection


    if ensure_mysql_connection(timeout_s=90):
        register_endpoints(app)
        
        load_dotenv(find_dotenv())

        app.run(
            host=os.getenv('APP_HOST', '0.0.0.0'),  # type: ignore
            port=os.getenv('APP_PORT', 7777),  # type: ignore
            debug=os.getenv('APP_DEBUG', True)  # type: ignore
        )
    
    else:
        raise DatabaseConnectionError
