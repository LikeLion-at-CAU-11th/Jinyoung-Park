from django.urls import path
from posts.views import *

urlpatterns = [
    path("", hello_world, name="hello_world"),
    path("all/", get_post_all, name="get_post_all"),
    path("<int:id>/", post_detail, name="post_detail"),
    path("new/", create_post, name="create_post"),
    path("comment/<int:post_id>/", comment, name="comment"),
    path("inTime/", get_post_in_time, name="get_post_in_time"),
]
