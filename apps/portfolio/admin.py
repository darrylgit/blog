from django.contrib import admin
from .models import Portfolio

# Register your models here.
@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
	fields = ('author', 'title', 'description', 'slug', 'brandname', 'brandlogo', 'brandtypeface', 'text', 'tags')
	prepopulated_fields = {'slug': ('title',)}
	list_display = ('title','author')