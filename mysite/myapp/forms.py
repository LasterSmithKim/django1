#-*- coding: utf-8 -*-
from django import forms
from .models import Dreamreal

class LoginForm(forms.Form):
   user = forms.CharField(max_length = 100)
   password = forms.CharField(widget = forms.PasswordInput())
   #尚有数据库验证没有完成


class ProfileForm(forms.Form):
   name = forms.CharField(max_length = 100)
   picture = forms.ImageField()