from django.db import models
from django.utils import timezone
from users.models import NewUser
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.conf import settings

class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add= True)
    name = models.CharField(max_length = 100, blank = False)

    def __str__(self):
        return self.name
    

class Posts(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, blank=False)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now_add= True)
    title = models.CharField(max_length = 100, blank= False)
    body = models.TextField(blank = False)
    slug = models.SlugField(max_length= 200, blank= False, null = False)
    tags = TaggableManager()
    
    def save(self, *args, **kwargs):
        self.slug =slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Images(models.Model):
    post = models.ForeignKey(Posts, on_delete= models.CASCADE, related_name ='images')
    image = models.ImageField(upload_to="posts")

    def __str__(self):
        return "%s" % (self.post.title)

