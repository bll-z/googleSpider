from django.conf.urls import patterns, url

from imageCrawler import views

urlpatterns = patterns('imageCrawler/',
	# ex: /imageCrawler/
	url(r'^$', views.index, name='index'),
	# ex: /imageCrawler/queries
	url(r'^queries/$', views.ImageQueryListView.as_view(), name='queries'),
	# ex: /imageCrawler/search
	url(r'^search/$', views.searchView, name='search'),
	# ex: /imageCrawler/query/id
	url(r'^query/(?P<pk>\d+)$', views.ImageQueryView.as_view(), name='query'),
	# ex: /imageCrawler/image/id
	url(r'^image/(?P<pk>\d+)$', views.ImageResultView.as_view(), name='image'),
)