from django.contrib import admin
from .models import Media

# Register your models here.
@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
	fields              = ('filepath', 'creator', 'source', 'media', 'alternate_text')