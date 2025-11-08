import os

import redis
import mysql.connector
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


mysql_host = os.getenv('MYSQL_HOST', '127.0.0.1')
mysql_port = int(os.getenv('MYSQL_PORT', 3306))
mysql_user = os.getenv('MYSQL_USER', 'root')
mysql_passwd = os.getenv('MYSQL_PASSWD', 'passwd')

redis_host = os.getenv('REDIS_HOST', '127.0.0.1')
redis_port = int(os.getenv('REDIS_PORT', 6379))


class RedisClient:
    """
    Redis client wrapper class
    """
    
    @classmethod
    def check_access(cls) -> bool:
        """
        Checks connection to Redis database
        
        :return: bool indicating connection status
        """
        try:
            redis.Redis(host=redis_host, port=redis_port, db=0).ping()
            return True
        
        except redis.ConnectionError:
            return False
    
    def __init__(self):
        self.client = redis.Redis(host=redis_host, port=redis_port, db=0)


class MySQLClient:
    """
    MySQL client wrapper class
    """
    @classmethod
    def check_access(cls) -> bool:
        """
        Checks connection to MySQL database
        
        :return: bool indicating connection status
        """
        try:
            connection = mysql.connector.connect(host=mysql_host, port=mysql_port, user=mysql_user, passwd=mysql_passwd)
            if connection.is_connected():
                connection.close()
                return True
            return False

        except mysql.connector.Error:
            return False
    
    def __init__(self):
        pass
