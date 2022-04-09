from django.conf.urls import include, url

from .views import WriteupIndexView, WriteupDetailView

app_name="writeup"

urlpatterns =[
	url(r'^writeup/$', WriteupIndexView.as_view(), name='index'),
	url(r'^writeup/(?P<slug>.*)/$', WriteupDetailView.as_view(), name='detail')
]