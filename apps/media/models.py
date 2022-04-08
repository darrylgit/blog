import os
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinLengthValidator

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_source_path(instance, filename):
    # filepath = '<creator id>/<model name>/<model id>/media/<media id>/<thumbnail, image, video>/source'
    return os.path.join("%s/%s/%s" % (
        instance.creator.id, 
        instance.filepath.strip('/'), 
        filename))

class Media(models.Model):
    filepath       = models.CharField(max_length=400) # required
    alternate_text = models.CharField(max_length=400, null=True, blank=True)

    source         = models.ImageField(upload_to=get_source_path, null=True, blank=True)

    # associations
    media          = models.ForeignKey('self', related_name="media_thumbnails", on_delete=models.CASCADE, null=True, blank=True)
    creator        = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Media'
        
    def __int__(self):
        return self.id