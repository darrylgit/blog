from django.contrib import admin
from .models import Writeup, WriteupMedia, WriteupSegment, WriteupSegmentMedia

# Register your models here.
@admin.register(Writeup)
class WriteupAdmin(admin.ModelAdmin):
	fields              = ('recap', 'author', 'title', 'description', 'slug', 'text', 'tags', 'created_at', 'updated_at', 'deleted_at')
	prepopulated_fields = {'slug': ('title',)}
	list_display        = ('title', 'author')

@admin.register(WriteupMedia)
class WriteupMediaAdmin(admin.ModelAdmin):
	fields              = ('writeup', 'media', 'rank')
	list_display        = ('writeup', 'media', 'rank')

@admin.register(WriteupSegment)
class WriteupSegmentAdmin(admin.ModelAdmin):
	fields              = ('writeup', 'rank', 'text', 'is_media')
	list_display        = ('writeup', 'rank', 'text', 'is_media')

@admin.register(WriteupSegmentMedia)
class WriteupSegmentMediaAdmin(admin.ModelAdmin):
	fields              = ('writeup_segment', 'media', 'rank')
	list_display        = ('writeup_segment', 'media', 'rank')