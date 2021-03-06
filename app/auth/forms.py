# _*_coding:utf-8_*_
from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,PasswordField
from wtforms.validators import DataRequired, length, Email, Regexp, EqualTo, ValidationError
from flask_wtf import FlaskForm
from ..models import User,Role

class LoginForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(), length(1, 64), Email()])
    password = PasswordField(u'密码', validators=[DataRequired()])
    verify = StringField(u"验证码",validators=[DataRequired()])
    remember_me = BooleanField(u'保持登录状态')
    submit = SubmitField(u'提交')



class RegisterForm(FlaskForm):
    email = StringField(u'邮箱', validators=[DataRequired(), Email(), length(1, 64)])
    username = StringField(u'用户名', validators=[DataRequired(),
                                                   length(1, 64),
                                                   Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0,
                                                          'Usernames must have only letters, '
                                                          'numbers, dots or underscores')])
    password = PasswordField(u'密码',
                             validators=[DataRequired(), EqualTo('password2', message='password is not match '), ])
    password2 = PasswordField(u'确认密码', validators=[DataRequired()])
    verify = StringField(u"验证码", validators=[DataRequired()])
    submit = SubmitField(u'注册')

    # 设置验证邮箱
    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')

    # 验证用户名
    def validate_username(self, field):
        if User.query.filter_by(name=field.data).first():
            raise ValidationError('Username is already in user')


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old password', validators=[DataRequired()])
    password = PasswordField('New password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm new password',
                              validators=[DataRequired()])
    submit = SubmitField('Update Password')


class PasswordResetRequestForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), length(1, 64),
                                             Email()])
    submit = SubmitField('Reset Password')


class PasswordResetForm(FlaskForm):
    password = PasswordField('New Password', validators=[
        DataRequired(), EqualTo('password2', message='Passwords must match')])
    password2 = PasswordField('Confirm password', validators=[DataRequired()])
    submit = SubmitField('Reset Password')


class ChangeEmailForm(FlaskForm):
    email = StringField('New Email', validators=[DataRequired(), length(1, 64),
                                                 Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Update Email Address')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

class UserInfo(FlaskForm):
    name = StringField(u'用户名:',validators=[DataRequired(),
                                                   length(2, 64),
                                                   Regexp('^.*$', 0,
                                                          'Usernames must have only letters, '
                                                          'numbers, dots or underscores')])
    # email = StringField(u'电子邮箱:',validators=[DataRequired(), length(6, 64),
    #                                              Email()])
    # comfirmed = BooleanField(u'认证:')
    submit =SubmitField(u"提交")