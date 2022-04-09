from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Writeup

class WriteupDetailView(DetailView):
	template_name      ='writeup/detail.html'
	context_object_name='writeup'
	model=Writeup
	context={}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class WriteupIndexView(ListView):
	template_name      ='writeup/index.html'
	context_object_name='writeup'
	model=Writeup
	context={}
	
	def get(self, request):
		self.context['writeups']= self.model.objects.all().order_by('-created_at')

		return render(request, self.template_name, self.context)