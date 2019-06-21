"""
文件名: utils.py
日期: 2019-03-23  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""
from functools import wraps

from flask import session, flash, redirect, url_for


def is_login(f):
    """用来判断用户是否登录成功"""

    @wraps(f)
    def wrapper(*args, **kwargs):
        # 判断session对象中是否有seesion['user'],
        # 如果包含信息， 则登录成功， 可以访问主页；
        # 如果不包含信息， 则未登录成功， 跳转到登录界面;；
        if session.get('user', None):
            return f(*args, **kwargs)
        else:
            flash("用户必须登录才能访问%s" % (f.__name__))
            return redirect(url_for('home.login'))

    return wrapper



def change_filename(filename):
    """在原有文件的基础上添加时间标签"""
    from datetime import  datetime
    return  datetime.now().strftime('%Y%m%d_%H%M%S') + filename
