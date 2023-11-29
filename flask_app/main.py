from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import UniqueConstraint

from produser import publish

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:root@db/main"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

CORS(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))


class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    UniqueConstraint('user_id', "product_id", name='user_product_unique')


@app.route('/')
def main():
    publish(1, 2)
    return jsonify({
        'flask': "3.0 endpoint"
    })


if __name__ == '__main__':
    app.run()
