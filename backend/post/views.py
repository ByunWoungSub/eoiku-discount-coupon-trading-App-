from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from django.http import JsonResponse
from rest_framework.response import Response
# Create your views here.


class PostListAPIView(APIView):
    def get(self,request):
        serializer = PostSerializer(Post.objects.all(),many=True)
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors,staus=400)


class PostDetailAPIView(APIView):
    def get_object(self,pk):
        return get_object_or_404(Post, pk=pk)

    def get(self,request,pk,format=None):
        post = self.get_object(pk)
        serializer=PostSerializer(post)
        return Response(serializer.data)

    def put(self,request,pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=400)
    
    def delete(self,request,pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=204)