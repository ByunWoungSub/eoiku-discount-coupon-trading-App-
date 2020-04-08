from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import Post,User_info,Coupon
from .serializers import *
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer