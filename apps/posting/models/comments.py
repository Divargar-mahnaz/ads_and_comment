from django.db import models
from apps.account.models import User
from apps.posting.models.ads import Advertising
from common.base_manager import BaseManager


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advertising = models.ForeignKey(Advertising, on_delete=models.CASCADE)
    content = models.TextField()
    objects = BaseManager()

    class Meta:
        unique_together = ('user', 'advertising')
