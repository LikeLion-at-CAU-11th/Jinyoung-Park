from django.contrib import admin
from .models import Post, Comment

# Register your models here.
admin.site.register(Post)  # 시간 추가 가능
admin.site.register(Comment)
