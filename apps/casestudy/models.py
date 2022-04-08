from django.db import models
from django.utils import timezone

from apps.writeup.models import Writeup

# Create your models here.
class CaseStudyWriteup(models.Model):
    writeup    = models.ForeignKey(Writeup, on_delete=models.CASCADE)
    
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def publish(self):
        self.created_at = timezone.now()
        self.save()

    def __int__(self):
        return self.id