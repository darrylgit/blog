from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.portfolio.models import Portfolio

# Create your models here.

class Mockup(models.Model):
	def lorem_default():
		return "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eligendi eos laboriosam et eius."

	FIRST, SECOND, THIRD = ('First', 'Second', 'Third')

	POSITION_CHOICES = (
		(FIRST, _('First')),
		(SECOND, _('Second')),
		(THIRD, _('Third')),
	)

	project = models.ForeignKey(Portfolio, related_name="mockups", on_delete=models.CASCADE)
	position = models.CharField(max_length=20, choices=POSITION_CHOICES, default=FIRST)
	title = models.CharField(max_length=200, null = True, default=lorem_default)
	alt = models.CharField(max_length=400, null=True, default=lorem_default)
	image = models.ImageField(upload_to = 'portfolio/img/', null = True)

	class Meta:
		verbose_name = 'Mockup'
		unique_together = (('project','position'),)

	def __str__(self):
		return self.title