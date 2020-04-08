from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .models import Post,User_info,Coupon
from .serializers import *
# Create your views here.


#Post
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


#User
class UserListView(generics.ListCreateAPIView):
    queryset = User_info.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User_info.objects.all()
    serializer_class = UserSerializer

#Coupon
class CouponListView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer


class CouponDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer