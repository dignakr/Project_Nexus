# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Login(models.Model):
	login_username = models.CharField(max_length=50)
	login_password = models.CharField(max_length=50)

class Signup(models.Model):
	login = models.ForeignKey(Login,on_delete=models.CASCADE)
	name = models.CharField(max_length=50)

class Verify(models.Model):
	login = models.ForeignKey(Login,on_delete=models.CASCADE)
	checkbox = models.CharField(max_length=50)
	
	
