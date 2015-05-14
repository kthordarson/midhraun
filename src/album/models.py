from django.db import models
from django.conf import settings

from horses.models import Horse


class Image(models.Model):
    horse = models.ForeignKey(Horse, null=True)
    image = models.ImageField(upload_to=settings.MEDIA_ROOT)
