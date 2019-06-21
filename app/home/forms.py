"""
文件名: forms.py
日期: 2019-03-17  
作者: lvah
联系: xc_guofan@qq.com
代码描述: 



"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, FileField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Email, Regexp
from flask_wtf.file import FileAllowed, FileRequired


class BaseForm(FlaskForm):
    username = StringField(
        label="用户名",
        validators=[
            DataRequired()

        ]
    )
    password = PasswordField(
        label="密码",
        validators=[
            DataRequired(),
            Length(6, 12, message="密码长度必须为0-12")

        ]
    )


class LoginForm(BaseForm):
    submit = SubmitField(
        label="登录"
    )


class RegisterForm(BaseForm):
    repassword = PasswordField(
        label="确认密码",
        validators=[
            EqualTo('password', message="两次密码不一致")
        ]
    )
    email = StringField(
        label="邮箱",
        validators=[
            Email(message="邮箱格式不正确")
        ]
    )

    submit = SubmitField(
        label="注册"
    )


class EditUserForm(FlaskForm):
    username = StringField(
        label="用户名",
        validators=[
            DataRequired()

        ]
    )
    email = StringField(
        label="邮箱",
        # validators=[
        #     Email(message="邮箱格式不正确")
        # ]
    )

    phone = StringField(
        label="电话",
        # validators=[
        #     Regexp(r'1\d{10}', message="电话号码格式不正确")
        # ]
    )

    submit = SubmitField(
        label="更新信息"
    )


class PwdForm(FlaskForm):
    old_pwd = PasswordField(
        label="旧密码",
        validators=[
            DataRequired()
        ],
        # <input name="xxx" placeholder="">
        render_kw={
            'placeholder': "请输入旧密码"
        }
    )
    new_pwd = PasswordField(
        label="新密码",
        validators=[
            DataRequired()
        ],
        render_kw={
            'placeholder': "请输入新密码"
        }
    )

    submit = SubmitField(
        label="修改密码"
    )


class UploadForm(FlaskForm):
    file = FileField(
        label="上传文件",
        validators=[
            # 文件必须选择;
            FileRequired(),
            # 指定文件上传的格式;
            FileAllowed(['xls', 'xlsx', 'csv'], '只接收Excel格式和csv格式的文件')
        ]
    )

    kind = SelectField(
        label="绘图种类",
        coerce=int,
        choices=[(1, "折线图"), (2, "散点图"), (3, '饼状图'), (4, '柱状图')]
    )

    element = SelectField(
        label="绘图指标",
        coerce=int,
        choices=[(1, "平均学分绩点"), (2, "学分绩点总和"), (3, '学分加权平均分')]
    )

    submit = SubmitField(label="上传文件",
                         render_kw={
                             'id': 'submit_btn'
                         })
