from django.contrib import admin

from core.models import CustomUser, Article


admin.site.register(CustomUser)
admin.site.register(Article)

# @admin.register(CustomUser):
# class CustomUserAdmin:
#     ...
