if __name__ == '__main__':
    import os
    import time

    from dotenv import find_dotenv, load_dotenv

    from create import app
    from endpoints import endpoints
    from database import RedisClient, MySQLClient

    endpoints.register_endpoints(app)
    
    while not (RedisClient.check_access() and MySQLClient.check_access()):
        time.sleep(5)
    
    load_dotenv(find_dotenv())

    app.run(
        host=os.getenv('APP_HOST'),  # type: ignore
        port=os.getenv('APP_PORT'),  # type: ignore
        debug=os.getenv('APP_DEBUG')  # type: ignore
    )
