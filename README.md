# 部署

- 安装python依赖包

```
pip install -r requirement.txt

```

- 修改config.py

```
# 修改用户名和密码， 数据库名
SQLALCHEMY_DATABASE_URI = "mysql://root:redhat@localhost/student"
```


- 初始化数据库

```
python3 manage.py initdb
```


- 开启服务
```
python3 manage.py runserver
```


- 浏览器访问`http://127.0.0.1:5000`



# 运行效果图


## 登录界面

![登录界面](./img/login.png)


## 注册界面
![注册界面](./img/register.png)


## 主页

![主界面](./img/index.png)


## 上传学生信息界面

![上传界面](./img/upload.png)


## 已上传班级分析效果

- 平均学分绩点

![](./img/avg.png)

- 学分绩点总和

![](./img/sum.png)

- 学分加权平均分

![](./img/wsum.png)













