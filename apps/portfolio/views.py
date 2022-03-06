from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Portfolio

class PortfolioIndexView(ListView):
	template_name='portfolio/index.html'
	context_object_name='portfolio'
	model=Portfolio
	context={}
	def get(self, request):
		self.context['project']= self.model.objects.all().order_by('-published_date')

		return render(request, self.template_name, {self.context_object_name:self.context})

class PortfolioDetailView(DetailView):
	model=Portfolio
	context_object_name='project'
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context