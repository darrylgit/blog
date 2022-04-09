from django.conf.urls import include, url

from .views import BlogIndexView, BlogDetailView, BlogWriteupIndexView, BlogWriteupDetailView

app_name="blog"

writeuppatterns =[
	url(r'^$', BlogIndexView.as_view(), name='writeup-index'),
	url(r'^(?P<slug>.*)/$', BlogDetailView.as_view(), name='writeup-detail')
]

urlpatterns =[
	url(r'^blog/$', BlogIndexView.as_view(), name='index'),
	url(r'^blog_writeup/', include(writeuppatterns))
]