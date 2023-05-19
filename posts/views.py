from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods
from .models import Post, Comment
import json

from .serializers import PostSerializer, CommentSerializer  # import 잊지 말자,,

# APIView를 사용하기 위해 import
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  # 상태코드를 넘겨줌
from django.http import Http404

# Create your views here.


class PostList(APIView):  # post는 보통 List(전체)에 넣는다
    def post(self, request, format=None):  # 이름은 Http 이름으로~ 알아듣기 편하게
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():  # DB는 소중하니까 건드릴 때는 valid 한지 확인해주는게 좋음~^^
            serializer.save()
            return Response(
                serializer.data, status=status.HTTP_201_CREATED
            )  # JSON으로 바꿔주지 않아도 알아서 해줌 so, 그냥 Response()
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetail(APIView):
    def get(self, request, id):
        post = get_object_or_404(Post, post_id=id)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, id):
        post = get_object_or_404(Post, post_id=id)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        post = get_object_or_404(Post, post_id=id)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentList(APIView):
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)


class CommentDetail(APIView):
    def get(self, request, post):
        comments = Comment.objects.filter(post=post)  # FK로 가져옴
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def put(self, request, post):
        comment = get_object_or_404(Comment, post=post)
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, post):
        comment = get_object_or_404(Comment, post=post)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
