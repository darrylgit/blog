from django.conf.urls import include, url

from .views import ProjectIndexView, ProjectDetailView

app_name="project"

urlpatterns =[
	url(r'^project/$', ProjectIndexView.as_view(), name='index'),
	url(r'^project/(?P<slug>.*)/$', ProjectDetailView.as_view(), name='detail'),
]