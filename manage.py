import os
import dotenv

# Load environment variable from a .env file
dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from jam import create_app, app

jam_app = create_app()
manager = Manager(jam_app)

# Migration commands for when you create DB
Migrate(jam_app, app.DB)
manager.add_command('db', MigrateCommand)

@manager.command
def run(port=5000):
	app.run(port=int(port))

if __name__ == "__main__":
	manager.run()