# Generated by Django 4.2.3 on 2023-07-29 03:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="thumbnail",
            field=models.ImageField(null=True, upload_to="", verbose_name="썸네일"),
        ),
    ]