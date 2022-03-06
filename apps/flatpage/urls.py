from django.conf.urls import include, url

from .views import IndexFlatpageView

app_name = 'flatpage'

urlpatterns =[
	url(r'^$', IndexFlatpageView.as_view(), name='index'),
]