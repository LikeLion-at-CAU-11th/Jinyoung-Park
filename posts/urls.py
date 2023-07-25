from django.urls import path, include
from posts.views import *
from rest_framework.routers import DefaultRouter


# router 사용 -> 자동으로 url 패턴 생성, viewset과 연결 so, .as_view() 안해도 됨
postRouter = DefaultRouter()
# postRouter.register("", PostViewSet, basename="Post")  # 이미 posts/를 해놔서 prefix 필요 없음

# key값을 받기 위해서 라우터 분리
# commentRouter = DefaultRouter()
# commentRouter.register("", CommentViewSet, basename="Comment")  # 라우터 분리하면 basename 필요


urlpatterns = [
    # path("", hello_world, name="hello_world"),
    # path("all/", get_post_all, name="get_post_all"),
    # path("<int:id>/", post_detail, name="post_detail"),
    # path("new/", create_post, name="create_post"),
    # path("comment/<int:post_id>/", comment, name="comment"),
    # path("inTime/", get_post_in_time, name="get_post_in_time"),
    # ---DRF---
    path("", PostList.as_view()),
    path("<int:id>/", PostDetail.as_view()),
    # path("<int:post>/comment", CommentDetail.as_view()),  # 입력받는 인자 이름 일치시켜야됨~
    # path("comment", CommentList.as_view()),
    # ---VeiwSet---
    # path("", post_list),
    # path("<int:pk>/", post_detail),
    # ---VeiwSet + Router---
    # path("", include(postRouter.urls)),
    # path("<int:id>/comment", include(commentRouter.urls)),
]
