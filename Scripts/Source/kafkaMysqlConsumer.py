import sys
import os
import mysql.connector
from kafka import KafkaConsumer

consumer = KafkaConsumer('my_favorite_topic')
for msg in consumer:
    print (msg)

