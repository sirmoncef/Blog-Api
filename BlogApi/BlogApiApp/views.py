from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Blog
from .serializers import BlogSerializers
from rest_framework.response import Response

@api_view(['GET'])
def list(request):
    blogs = Blog.objects.all()
    serializer = BlogSerializers(blogs, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create(request):
    serializer = BlogSerializers(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['POST'])
def update(request,pk):
    blogs = Blog.objects.get(pk=pk)
    serializer = BlogSerializers(instance=blogs,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)


@api_view(['DELETE'])
def delete(request,pk):
    blogs = Blog.objects.get(pk=pk)
    blogs.delete()
    return Response('deleted')


