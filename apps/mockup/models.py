from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.project.models import Project

# Create your models here.

class Mockup(models.Model):
	def lorem_default():
		return "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi eos laboriosam et eius."

	FIRST, SECOND, THIRD = ('First', 'Second', 'Third')

	RANK_CHOICES = (
		(FIRST, _('First')),
		(SECOND, _('Second')),
		(THIRD, _('Third')),
	)

	project         = models.ForeignKey(Project, related_name="mockups", on_delete=models.CASCADE)
	rank            = models.CharField(max_length=20, choices=RANK_CHOICES, default=FIRST)
	alternate_text  = models.CharField(max_length=400, null=True)
	source          = models.ImageField(upload_to='mockup/images/', null=True)

	class Meta:
		verbose_name = 'Mockup'
		unique_together = (('project','rank'),)
		
	def __int__(self):
		return self.id