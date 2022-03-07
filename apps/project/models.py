from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from taggit.managers import TaggableManager


# Create your models here.
class Project(models.Model):
    def lorem_default():
        return "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi eos laboriosam et eius."

    brandname     = models.CharField(max_length=200, null=True)
    recap         = models.TextField(null=True)

    brandlogo     = models.ImageField(upload_to='project/images/', null=True)
    brandtypeface = models.ImageField(upload_to='project/images/', null=True)

    text          = models.TextField(null=True, blank=True)
    author        = models.ForeignKey(User, on_delete=models.CASCADE)

    title         = models.CharField(max_length=200, null=True)
    description   = models.CharField(max_length=400, null=True)

    tags = TaggableManager(blank=True)
  
    slug = models.SlugField(unique=True)
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __int__(self):
        return self.id