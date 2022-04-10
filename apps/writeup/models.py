from django.contrib.auth.models import User
from django.utils import timezone

from taggit.managers import TaggableManager

from django.db import models
from apps.media.models import Media

# Create your models here.
class Writeup(models.Model):
    def lorem_default():
        return "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi eos laboriosam et eius."

    recap         = models.TextField(null=True)
    
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

class WriteupMedia(models.Model):
    rank       = models.DecimalField(max_digits=3, decimal_places=2)
    media      = models.ForeignKey(
        Media, 
        related_name="writeup_medias", 
        on_delete=models.CASCADE)

    writeup       = models.ForeignKey(
        Writeup, 
        related_name="writeup_medias", 
        on_delete=models.CASCADE)

    def __int__(self):
        return self.id

class WriteupSegment(models.Model):
    # segment of writeup, ie paragraphs or media
    # segment may be group of text, photos, or videos
    rank         = models.DecimalField(max_digits=3, decimal_places=2)
    text         = models.TextField(null=True, blank=True)

    is_media     = models.BooleanField(default=False)

    writeup      = models.ForeignKey(
        Writeup, 
        related_name="writeup_segments", 
        on_delete=models.CASCADE)

    def __int__(self):
        return self.id

class WriteupSegmentMedia(models.Model):
    rank            = models.DecimalField(max_digits=3, decimal_places=2)
    media           = models.ForeignKey(
        Media, 
        related_name="writeup_segment_medias", 
        on_delete=models.CASCADE)

    writeup_segment = models.ForeignKey(
        WriteupSegment, 
        related_name="writeup_segment_medias", 
        on_delete=models.CASCADE)

    def __int__(self):
        return self.id