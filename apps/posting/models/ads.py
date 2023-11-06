from django.db import models
from apps.account.models import User
from common.base_manager import BaseManager


class Advertising(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    objects = BaseManager()
