
from django.shortcuts import render,get_object_or_404
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.response import Response
# Create your views here.


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
