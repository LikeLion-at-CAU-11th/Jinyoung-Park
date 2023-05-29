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

# DRF~
# class PostList(APIView):  # post는 보통 List(전체)에 넣는다
#     def post(self, request, format=None):  # 이름은 Http 이름으로~ 알아듣기 편하게
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():  # DB는 소중하니까 건드릴 때는 valid 한지 확인해주는게 좋음~^^
#             serializer.save()
#             return Response(
#                 serializer.data, status=status.HTTP_201_CREATED
#             )  # JSON으로 바꿔주지 않아도 알아서 해줌 so, 그냥 Response()
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def get(self, request, format=None):
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(serializer.data)


# class PostDetail(APIView):
#     def get(self, request, id):
#         post = get_object_or_404(Post, post_id=id)
#         serializer = PostSerializer(post)
#         return Response(serializer.data)

#     def put(self, request, id):
#         post = get_object_or_404(Post, post_id=id)
#         serializer = PostSerializer(post, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         post = get_object_or_404(Post, post_id=id)
#         post.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class CommentList(APIView):
#     def get(self, request, format=None):
#         comments = Comment.objects.all()
#         serializer = CommentSerializer(comments, many=True)

#         return Response(serializer.data)


# class CommentDetail(APIView):
#     def get(self, request, post):
#         comments = Comment.objects.filter(post=post)  # FK로 가져옴
#         serializer = CommentSerializer(comments, many=True)

#         return Response(serializer.data)

#     def post(self, request, post):
#         serializer = CommentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def put(self, request, post):
#         comment = Comment.objects.filter(post=post).first()  # first -> 먼저 쓴 댓글 수정~
#         serializer = CommentSerializer(comment, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, post):
#         comment = Comment.objects.filter(post=post).first()  # 먼저 쓴 댓글 삭제
#         comment.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# mixin~~~
# from rest_framework import mixins
# from rest_framework import generics


# class PostListMixins(
#     mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
# ):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class PostDetailMixins(
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin,
#     generics.GenericAPIView,
# ):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# genericsAPIView~
# class PostListGenericAPIView(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class PostDetailGenericAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# Veiwset~
from rest_framework import viewsets


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    # 라우터를 분리했기 때문에 post_id에 달린 comment를 반환하는 메서드 생성
    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs["id"])


# router의 사용으로 필요 없어짐
# post_list = PostViewSet.as_view(
#     {
#         "get": "list",
#         "post": "create",
#     }
# )

# post_detail = PostViewSet.as_view(
#     {
#         "get": "retrieve",
#         "put": "update",
#         "patch": "partial_update",
#         "delete": "destroy",
#     }
# )
