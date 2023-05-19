from django.urls import path
from posts.views import *

urlpatterns = [
    # path("", hello_world, name="hello_world"),
    # path("all/", get_post_all, name="get_post_all"),
    # path("<int:id>/", post_detail, name="post_detail"),
    # path("new/", create_post, name="create_post"),
    # path("comment/<int:post_id>/", comment, name="comment"),
    # path("inTime/", get_post_in_time, name="get_post_in_time"),
    path("", PostList.as_view()),
    path("<int:id>/", PostDetail.as_view()),
    path("<int:post>/comment", CommentDetail.as_view()),  # 입력받는 인자 이름 일치시켜야됨~
    path("comment", CommentList.as_view()),
]
