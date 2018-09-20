#!/usr/bin/python
import random
import json
from time import sleep
from json import dumps
from mysqlConnection import Mysqlcon

from kafka import KafkaProducer


# Import test data
obj = Mysqlcon()
TEST_DATA = obj.getData()

print (TEST_DATA)
    
# Set up producer
PRODUCER = KafkaProducer(
    bootstrap_servers='localhost:9092',
    client_id='test-producer'
)

TOPIC = 'my_favorite_topic'

LOOP = True

while LOOP:
    rec = TEST_DATA

    try:
        PRODUCER.send(TOPIC, json.dumps(rec).encode('utf-8'))
    except UnicodeDecodeError:
        pass

    print('pushed: %s' % rec)

    # Send records at random intervals; adjust this to send more or less frequently
    sleep(random.uniform(0.01, 5))