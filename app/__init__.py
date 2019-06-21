from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_moment import Moment  # 时间的问题解决
from flask_bootstrap import Bootstrap  # 导入bootstrap样式
from flask_migrate import  Migrate

app = Flask(__name__)
manager = Manager(app)
bootstrap = Bootstrap(app)

# 数据库报错问题
pymysql.install_as_MySQLdb()
# 读取配置文件的配置信息
app.config.from_pyfile('../config.py')
db = SQLAlchemy(app)
moment = Moment(app)
migrate = Migrate(app, db)


from app.home import home as home_blueprint

# 注册admin蓝图, url_prefix='/admin'添加前缀/admin
# 注册home蓝图, 不添加前缀
app.register_blueprint(home_blueprint)
