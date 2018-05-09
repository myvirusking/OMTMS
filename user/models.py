from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class MyUser(models.Model):
    myuser=models.OneToOneField(User,on_delete=models.CASCADE)
    type = models.CharField(max_length=10, default="user")
    
    def __str__(self):
        return "{0}({1})".format(self.myuser.username,self.type)


class MovieTheater(models.Model):
    theatername=models.CharField(max_length=60)
    theaterplace=models.CharField(max_length=20)

    def __str__(self):
        return "{0}({1})".format(self.theatername,self.theaterplace)
    
class MovieName(models.Model):
    theater=models.ForeignKey(MovieTheater, on_delete=models.CASCADE)
    moviename=models.CharField(max_length=50)
    language=models.CharField(max_length=10,default="Hindi")
    totaltickets=models.IntegerField(default=120)
    availabletickets=models.IntegerField(default=0)
    ticketprice=models.IntegerField(default=100)
    
    def __str__(self):
        return "{0}({1}-{2})".format(self.moviename,self.theater.theatername,self.theater.theaterplace)
    

class MovieTicket(models.Model):
    ticketuser=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    moviename=models.OneToOneField(MovieName,on_delete=models.CASCADE)
    moviedate=models.DateField()
    movietime=models.TimeField()
    bookingtime=models.DateTimeField(default=datetime.datetime.now())
    quantity=models.IntegerField()
    totalprice=models.IntegerField()

    def __str__(self):
        return "{0}({1}-{2})".format(self.moviename.moviename,self.ticketuser.myuser.username,self.moviedate)
    
    