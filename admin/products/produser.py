import json

import pika

params = pika.ConnectionParameters(
    host='host.docker.internal',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials('guest', 'guest')
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main', durable=True)


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)
