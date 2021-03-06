from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app.models import User,Article,Role
#create app instances

app=create_app('production')
manager=Manager(app)
migrate=Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.shell
def make_shell_context():
    return dict(app=app,db=db,User=User,Article=Article,Role=Role)

@manager.command
def test():
    import unittest




if __name__=='__main__':
    manager.run()
