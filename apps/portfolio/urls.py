from django.conf.urls import include, url

from .views import PortfolioIndexView, PortfolioDetailView

app_name="portfolio"

urlpatterns =[
	url(r'^portfolio/$', PortfolioIndexView.as_view(), name='index'),
	url(r'^portfolio/(?P<slug>.*)/$', PortfolioDetailView.as_view(), name='detail'),
]