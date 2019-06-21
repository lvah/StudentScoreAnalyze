from app import manager
# from app.models import  *
from app import  db
from werkzeug.security import  generate_password_hash

from app.models import User
from flask_migrate import  MigrateCommand


@manager.command
def initdb():
    """初始化数据库表"""
    db.drop_all()
    db.create_all()
    u = User(name='westos', password=generate_password_hash('westos'))
    db.session.add(u)
    db.session.commit()
    print("初始化数据库成功......")



manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()