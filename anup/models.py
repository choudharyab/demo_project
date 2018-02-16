import os
from django.db import models



from tecture import settings


class User(models.Model):

    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    birth_date = models.DateField()
    address = models.CharField(max_length=30)
    image=models.ImageField(upload_to='profile.image',blank=True)
    status=models.IntegerField(default=0)

class admin1(models.Model):
    username=models.CharField(max_length=50)
    password=models.CharField(max_length=20)
    fullname=models.CharField(max_length=120)

class Role(models.Model):

    username=models.CharField(max_length=120)
    first_name=models.CharField(max_length=120)
    email=models.CharField(max_length=120)
    role=models.CharField(max_length=120)

class right(models.Model):

    Edit=models.CharField(max_length=120)
    Delete = models.CharField(max_length=120)
    Display= models.CharField(max_length=120)
    Add= models.CharField(max_length=120)
    role=models.ForeignKey(Role,on_delete=models.CASCADE)
    email=models.ForeignKey(User,on_delete=models.CASCADE)
    #role.id=models.ForeignKey(Role)



class  Profile(models.Model):


   name=models.CharField(max_length=120)
   email=models.EmailField(max_length=120)
   #birth_date=models.DateField(blank=True)
   #birth_date= models.DateField()
   gender = (("M", "Male"), ("F", "Female"),)
   address=models.CharField(max_length=30)
   father_name=models.CharField(max_length=120)
   mother_name=models.CharField(max_length=120)
   gender=models.CharField(max_length=1,choices=gender,default="M", null=False)
   image=models.ImageField(upload_to='\\Profile\\',blank=True,null=False)

class Article(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.ImageField(upload_to='upload')

class work(models.model):
    Date=models.DateField()
    froms=models.DateField()
    to=models.DateField()

