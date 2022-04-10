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

	def get_object(self, queryset=None):
		"""
		Return the object the view is displaying.
		
		Require `self.queryset` and a `pk` or `slug` argument in the URLconf.
		Subclasses can override this to return any object.
		"""
		# Use a custom queryset if provided; this is required for subclasses
		# like DateDetailView
		if queryset is None:
			queryset = self.get_queryset()
			
		# Next, try looking up by primary key.
		pk = self.kwargs.get(self.pk_url_kwarg)
		slug = self.kwargs.get(self.slug_url_kwarg)
		if pk is not None:
			queryset = queryset.filter(writeup__pk=pk)
			
		# Next, try looking up by slug.
		if slug is not None and (pk is None or self.query_pk_and_slug):
			slug_field = self.get_slug_field()
			queryset = queryset.filter(**{ 'writeup__%s' % (slug_field): slug })
			
		# If none of those are defined, it's an error.
		if pk is None and slug is None:
			raise AttributeError(
				"Generic detail view %s must be called with either an object "
				"pk or a slug in the URLconf." % self.__class__.__name__
			)
		try:
			# Get the single item from the filtered queryset
			obj = queryset.get()
		except queryset.model.DoesNotExist:
			raise Http404(_("No %(verbose_name)s found matching the query") %
					{'verbose_name': queryset.model._meta.verbose_name})
		return obj

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