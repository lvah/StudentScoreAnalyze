# 数据库配置信息
import os

SQLALCHEMY_DATABASE_URI = "mysql://root:redhat@localhost/student"
SQLALCHEMY_TRACK_MODIFICATIONS = True


# 表单的配置(CSRF)
SECRET_KEY = "WESTOS"


# 用户上传信息存储位置的配置
BASEDIR = os.path.abspath(os.path.dirname(__file__))   # 获取当前项目所在目录的绝对路径/root/PycharmProjects/day38_MovieProject
# /root/PycharmProjects/day38_MovieProject/app/static/upload/userFaceImg/
UPLOAD_FILE_DIR = os.path.join(BASEDIR, 'app/static', 'upload/files/')



# 分页的配置
PER_PAGE = 5