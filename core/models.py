from datetime import datetime

import django.utils.timezone
from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.conf import settings

from core.utils.utils import get_path_upload_avatar, get_path_upload_article_img, validate_size_image


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """Custom user model"""
    ROLE = [('subscriber', 'Subscriber'), ('author', 'Author')]

    email = models.EmailField(verbose_name='Email', db_index=True, unique=True)
    username = models.CharField(verbose_name='Username', db_index=True, max_length=255, unique=True)
    first_name = models.CharField(verbose_name='First name', max_length=30)
    last_name = models.CharField(verbose_name='Last name', max_length=150)
    role = models.CharField(choices=ROLE, max_length=10, verbose_name='Role')
    avatar = models.ImageField(
        upload_to=get_path_upload_avatar,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    created_at = models.DateTimeField(verbose_name='created at', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='update at', auto_now=True, editable=False)
    is_active = models.BooleanField(verbose_name='is active', default=True)
    is_staff = models.BooleanField(verbose_name='is staff', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    @property
    def fullname(self):
        return f'<{self.first_name} {self.last_name}>'


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name='Tittle')
    description = models.CharField(max_length=1027, verbose_name='Descriptions')
    body = models.TextField(verbose_name='Body')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Author')
    created_at = models.DateTimeField(default=django.utils.timezone.now, editable=False)
    image = models.ImageField(
        upload_to=get_path_upload_article_img,
        blank=True,
        null=True,
        validators=[FileExtensionValidator(allowed_extensions=['jpg']), validate_size_image]
    )

    is_open = models.BooleanField(default=True, verbose_name='Open article')

    objects = models.Manager()
