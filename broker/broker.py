import os

from confluent_kafka.admin import AdminClient


kafka_host = os.getenv('BROKER_HOST', '127.0.0.1')
kafka_port = int(os.getenv('BROKER_PORT', 7772))


class KafkaClient:
    """
    Kafka client wrapper class
    """
    
    @classmethod
    def check_access(cls) -> None:
        """
        Checks connection to Redis database
        
        :return: bool indicating connection status
        """
        print({'bootstrap.servers': f'{kafka_host}:{kafka_port}'})
        admin_client = AdminClient({'bootstrap.servers': f'{kafka_host}:{kafka_port}'})
        print(admin_client.list_topics().topics)
    
    def __init__(self):
        pass
        # self.client = redis.Redis(host=redis_host, port=redis_port, db=0)