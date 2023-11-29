
from flask_migrate import Migrate
from main import app, db

migrate = Migrate(app, db)

@app.cli.command('create-db')
def create_db():
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run()