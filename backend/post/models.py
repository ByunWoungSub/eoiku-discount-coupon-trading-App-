from django.db import models
import sys
sys.path.append("..")
from account.models import User
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    image = models.ImageField(upload_to='%Y/%m/%d')
    category = models.CharField(max_length=10,default="")
    period = models.DateField()
    price = models.IntegerField(default=0)
    state = models.BooleanField()

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['created']
        