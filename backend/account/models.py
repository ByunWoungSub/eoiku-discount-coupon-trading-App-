from django.db import models

# Create your models here.


class User(models.Model):
    
    id = models.CharField(max_length=30,primary_key=True)
    pw = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=50)
    phonenum = models.CharField(max_length=13)

    def __str__(self):
        return self.id

