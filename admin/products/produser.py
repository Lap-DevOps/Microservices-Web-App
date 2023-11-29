import pika

params = pika.ConnectionParameters(
    host='host.docker.internal',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials('guest', 'guest')
)

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    channel.basic_publish(exchange='', routing_key='admin', body=str(body))
