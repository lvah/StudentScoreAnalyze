from flask import  Blueprint


# 定义蓝图
home = Blueprint("home", __name__)

from app.home.views import  *



