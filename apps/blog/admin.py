from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	fields = ('author', 'title', 'description', 'slug', 'image', 'link', 'text', 'tags')
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title','author')