from django.db import models

# Create your models here.


class User_info(models.Model):
    
    id = models.CharField(max_length=30,primary_key=True)
    passwd = models.CharField(max_length=30)
    nickname = models.CharField(max_length=20,unique=True)
    email = models.CharField(max_length=50)
    phonenum = models.CharField(max_length=13)

    def __str__(self):
        return self.nickname



class Coupon(models.Model):
    image = models.ImageField(upload_to='%Y/%m/%d')
    category = models.CharField(max_length=10)
    period = models.DateField()
    price = models.IntegerField(default=0)


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User_info,on_delete=models.CASCADE)
    content = models.TextField()
    coupon = models.ForeignKey(Coupon,on_delete=models.SET_NULL,null=True)
    created = models.DateTimeField(auto_now_add=True)
    state = models.BooleanField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']


