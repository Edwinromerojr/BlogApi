from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response({"Success": "The setup was successful"})

@api_view(['GET'])
def getAllPosts(request):
    get_posts = Post.objects.all()
    serializer = PostSerializer(get_posts, many=True)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def createPost(request):
    data = request.data
    serializer = PostSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"Success": "The setup was successful"}, status=201)
    else:
        return Response(serializer.errors, status=400)    
    
@api_view(['DELETE'])
def deletePost(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        post.delete()
        return Response({"Success": "The post was successfully deleted"}, status=204)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)
    
@api_view(['GET'])
def getPost(request):
    post_id = request.data.get('post_id')
    try:
        post = Post.objects.get(id=post_id)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)
    
@api_view(['PUT'])
def updatePost(request):
    post_id = request.data.get('post_id')
    get_new_title = request.data.get('new_title')
    get_new_content = request.data.get('new_content')

    try:
        post = Post.objects.get(id=post_id)

        if get_new_title:
            post.title = get_new_title
        if get_new_content:
            post.content = get_new_content

        post.save()
        return Response({"Success": "The post was successfully updated"}, status=200)

    except Post.DoesNotExist:
        return Response({"Error": "The post does not exist"}, status=404)