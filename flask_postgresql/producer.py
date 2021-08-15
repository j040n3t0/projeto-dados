# compose_flask/app.py
from kafka import KafkaProducer
import logging
logging.basicConfig(level=logging.INFO)

producer = KafkaProducer(bootstrap_servers='host.docker.internal:9094')
future = producer.send('flask', b'teste-web')
producer.flush()