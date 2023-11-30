import pika

params = pika.ConnectionParameters(
    host='host.docker.internal',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials('guest', 'guest')
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin', durable=True)


def callback(ch, method, properties, body):
    print(f'Receive in admin: ', body)


channel.basic_consume(queue='admin', on_message_callback=callback)

print("Consuming admin")
print(channel.connection.channel())

channel.start_consuming()

# channel.close()