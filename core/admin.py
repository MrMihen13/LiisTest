from django.contrib import admin

from core.models import CustomUser, Article


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email', 'role', 'first_name', 'last_name', 'is_superuser', 'is_staff', 'is_active']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'description', 'is_open']
