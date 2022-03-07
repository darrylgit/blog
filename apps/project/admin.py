from django.contrib import admin
from .models import Project

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
	fields              = ('author', 'recap', 'created_at', 'updated_at', 'deleted_at', 'title', 'description', 'slug', 'brandname', 'brandlogo', 'brandtypeface', 'text', 'tags')
	prepopulated_fields = {'slug': ('title',)}
	list_display        = ('title','author')