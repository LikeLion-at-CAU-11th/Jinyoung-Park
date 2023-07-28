from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Member(AbstractUser):
    id = models.AutoField(primary_key=True)
    age = models.IntegerField(verbose_name="나이", default=20, null=True)
