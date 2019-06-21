"""
文件名: models.py
日期: 2019-03-17  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from datetime import datetime
from app import db

# 会员管理数据库
class User(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(300))
    email = db.Column(db.String(50), unique=True)  # 邮箱地址
    phone = db.Column(db.String(20), unique=True) # ********电话号码不能使用整形
    gender = db.Column(db.Boolean)  # 性别


    # 添加简介这一列信息
    info = db.Column(db.Text)


    def verify_password(self, password):
        from werkzeug.security import  check_password_hash
        # 判断密码是否正确
        return  check_password_hash(self.password, password)

    def __repr__(self):
        return "<User %s>" % (self.name)

