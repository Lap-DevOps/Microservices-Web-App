import json
import os

import django
import pika

import sys
sys.path.insert(0, '/app')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from django.apps import apps

# Вывести список всех зарегистрированных моделей
for model in apps.get_models():
    print(model)


from products.models import Product

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

channel.queue_declare(queue='admin', durable=True)


def callback(ch, method, properties, body):
    print('Received in admin')
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased!')


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()
