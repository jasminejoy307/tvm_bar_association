from django.db import models

# Create your models here.
class registration(models.Model):
    name=models.CharField(max_length=20)
    mobileno=models.CharField(max_length=50)
    email=models.EmailField(max_length=20)
    types=models.CharField(max_length=20)
    officeadd=models.CharField(max_length=50)
    residenceadd=models.CharField(max_length=50)
    joiningdate=models.DateField()
    duration=models.CharField(max_length=10)
    approvedate=models.DateField(null=True,blank=True)
    expirydate=models.DateField(null=True,blank=True)
    status=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=20,null=True,blank=True)


class meta:
    db_table='registration'

class admin(models.Model):
    email=models.EmailField(max_length=20)
    password=models.CharField(max_length=20)

class meta:
    db_table='admin'

class contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    subject=models.CharField(max_length=50)
    message=models.CharField(max_length=100)
    status=models.CharField(max_length=10,null=True,blank=True,default='off')

class meta:
    db_table='contact'