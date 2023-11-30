import json

import pika

from main import Product, db, app

params = pika.ConnectionParameters(
    host='host.docker.internal',
    port=5672,
    virtual_host='/',
    credentials=pika.PlainCredentials('guest', 'guest')
)

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='main', durable=True, )


def callback(ch, method, properties, body):
    print(f'Receive in main: ')
    data = json.loads(body)
    print(data)
    if properties.content_type == 'product_created':
        with app.app_context():
            product = Product(id=data['id'], title=data['title'], image=data['image'])
            db.session.add(product)
            db.session.commit()
        print('Product created')

    elif properties.content_type == 'product_updated':
        with app.app_context():
            product = Product.query.get(data["id"])
            product.title = data['title']
            product.image = data["image"]
            db.session.commit()
        print('Product updated')

    elif properties.content_type == 'product_deleted':
        with app.app_context():
            product = Product.query.get(data)
            db.session.delete(product)
            db.session.commit()
        print('Product deleted')


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print("Consuming")

channel.start_consuming()

# channel.close()
