from django.core.exceptions import ValidationError
from django.db import models

from apps.posting.exceptions import ObjectNotFound


class BaseManager(models.Manager):
    def get_object(self, **keyword):
        try:
            return self.get(**keyword)
        except (self.model.DoesNotExist, ValidationError):
            raise ObjectNotFound
