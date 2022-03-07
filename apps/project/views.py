from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Project

class ProjectIndexView(ListView):
	template_name      ='project/index.html'
	context_object_name='project'
	model=Project
	context={}
	
	def get(self, request):
		self.context['projects']= self.model.objects.all().order_by('-created_at')

		return render(request, self.template_name, self.context)

class ProjectDetailView(DetailView):
	template_name      ='project/detail.html'
	context_object_name='project'
	model=Project
	context={}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context