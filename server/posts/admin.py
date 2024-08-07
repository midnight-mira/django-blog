from django.contrib import admin
from posts.models import Category, Posts
from django.contrib.auth.admin import UserAdmin
# Register your models here.

admin.site.register(Category)
admin.site.register(Posts)