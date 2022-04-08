from django.db import models
from django.utils import timezone

from apps.media.models import Media
from apps.writeup.models import Writeup

# Create your models here.
class Blog(models.Model):
    recap      = models.TextField(null=True)
    text       = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __int__(self):
        return self.id

class BlogMedia(models.Model):
    rank       = models.DecimalField(max_digits=3, decimal_places=2)
    media      = models.ForeignKey(
        Media, 
        related_name="blog_medias", 
        on_delete=models.CASCADE)

    blog       = models.ForeignKey(
        Blog, 
        related_name="blog_medias", 
        on_delete=models.CASCADE)

    def __int__(self):
        return self.id

class BlogWriteup(models.Model):
    writeup    = models.ForeignKey(
        Writeup, 
        related_name="blog_writeups", 
        on_delete=models.CASCADE)

    blog       = models.ForeignKey(
        Blog, 
        related_name="blog_writeups", 
        on_delete=models.CASCADE)

    def __int__(self):
        return self.id