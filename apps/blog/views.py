from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Blog, BlogWriteup

class BlogDetailView(DetailView):
	template_name      ='blog/detail.html'
	context_object_name='blog'
	model=Blog
	context={}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class BlogIndexView(ListView):
	template_name      ='blog/index.html'
	context_object_name='blog'
	model=Blog
	context={}
	
	def get(self, request):
		self.context['blogs']= self.model.objects.all().order_by('-created_at')

		return render(request, self.template_name, self.context)

class BlogWriteupDetailView(DetailView):
	template_name      ='blog_writeup/detail.html'
	context_object_name='blog_writeup'
	model=BlogWriteup
	context={}

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		return context

class BlogWriteupIndexView(ListView):
	template_name      ='blog_writeup/index.html'
	context_object_name='blog_writeup'
	model=BlogWriteup
	context={}
	
	def get(self, request):
		self.context['blog_writeups']= self.model.objects.all().order_by('-created_at')

		return render(request, self.template_name, self.context)