from django.contrib import admin
from .models import Writeup

# Register your models here.
@admin.register(Writeup)
class WriteupAdmin(admin.ModelAdmin):
	fields              = ('recap', 'author', 'title', 'description', 'slug', 'text', 'tags', 'created_at', 'updated_at', 'deleted_at')
	prepopulated_fields = {'slug': ('title',)}
	list_display        = ('title', 'author')