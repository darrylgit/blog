from django.contrib import admin
from .models import Blog, BlogWriteup

# Register your models here.
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
	fields              = ('created_at', 'updated_at', 'deleted_at')

@admin.register(BlogWriteup)
class BlogWriteupAdmin(admin.ModelAdmin):
	fields              = ('blog', 'writeup')
	list_display        = ('blog', 'writeup')