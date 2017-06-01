from __future__ import unicode_literals
from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]')

class UserManager(models.Manager):
  def validate(self, postData):
    if len(postData['username']) < 8:
        print 1  #change this to message
        return False
    if not NAME_REGEX.match(postData['username']):
        print 2 #change this to message
        return False
    if not EMAIL_REGEX.match(postData['email']):
        print 3 #change this to message
        return False
    if len(postData['password']) < 8:
        print 4 #change this to message
        return False
    if postData['password'] != postData['confirm_pw']:
        print 5 #change this to message
        return False
    return True
  def login(self, postData):
    email1 = postData['email']
    password1 = postData['password']
    user1 = User.objects.filter(email=email1).first()
    print user1.password, password1
    if user1:
      if user1.password == password1:
        return True
    return False

class User(models.Model):
  username = models.CharField(max_length=38)
  email = models.CharField(max_length=38, default=None, null=True)
  password = models.CharField(max_length=38, default=None, null=True)  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  objects = UserManager() 


