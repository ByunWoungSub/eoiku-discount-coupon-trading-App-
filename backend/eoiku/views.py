from django.shortcuts import render,get_object_or_404
from rest_framework import viewsets
from .models import Post,User_info,Coupon
from .serializers import *
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User_info.objects.all()
    serializer_class = PostSerializer

class CouponPostViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = PostSerializer