from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post,User_info,Coupon
from .serializers import *
# Create your views here.


class PostListAPIView(APIView):
    def get(self, request):
        serializer = PostSerializer(Post.objects.all(),many=True)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors, status=400)


