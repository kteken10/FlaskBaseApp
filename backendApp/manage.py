from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from main import app, db

# Créer une instance de l'objet Manager
manager = Manager(app)

# Configurer l'extension de migration
migrate = Migrate(app, db)

# Ajouter les commandes de migration à l'objet Manager
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
