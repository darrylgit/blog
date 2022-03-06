from django.contrib import admin
from .models import Mockup

# Register your models here.
@admin.register(Mockup)
class MockupAdmin(admin.ModelAdmin):
	pass