from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyUser(models.Model):
    myuser=models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=10, default="user")
    
    def __str__(self):
        return "{0}({1})".format(self.myuser.username,self.type)