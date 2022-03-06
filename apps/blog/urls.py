from django.conf.urls import include, url

from .views import BlogProjectIndexView

app_name="blog"

urlpatterns =[
	url(r'^projects/$', BlogProjectIndexView.as_view(), name='project_index'),
]