from django.contrib.auth.models import AbstractUser
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill


class User(AbstractUser):
    email = models.EmailField('Email', null=True, blank=True, max_length=255)
    phone = models.CharField('Телефон', null=True, blank=True, max_length=18)
    age = models.PositiveIntegerField('Возраст', null=True, blank=True)
    avatar = models.ImageField(upload_to='avatars')
    avatar_thumbnail = ImageSpecField(
        format='JPEG', source='avatar', options={'quality': 80},
        processors=[ResizeToFill(100, 50)])

    def __str__(self):
        return self.username
