# Generated by Django 4.1.7 on 2023-07-11 06:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일시"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정일시"),
                ),
                ("post_id", models.AutoField(primary_key=True, serialize=False)),
                ("writer", models.CharField(max_length=30, verbose_name="작성자")),
                ("content", models.TextField(verbose_name="내용")),
                (
                    "category",
                    models.CharField(
                        choices=[("DIARY", "일기"), ("STUDY", "공부"), ("ETC", "기타")],
                        max_length=20,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일시"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정일시"),
                ),
                ("writer", models.CharField(max_length=30, verbose_name="작성자")),
                ("content", models.CharField(max_length=200, verbose_name="내용")),
                (
                    "post",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.post"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
