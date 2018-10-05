#-*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
#尚有数据库数据验证没有完成