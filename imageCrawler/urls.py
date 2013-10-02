from django.conf.urls import patterns, url

from imageCrawler import views

urlpatterns = patterns('',
	# ex: /imageCrawler/
	url(r'^$', views.index, name='index'),
	# ex: /imageCrawler/query/all/
	url(r'^query/all/$', views.ImageQueryListView.as_view(), name='all'),
	# ex: /imageCrawler/query/all/delete/
	url(r'^query/all/delete/$', views.delAll, name='delete:all'),
	# ex: /imageCrawler/search
	url(r'^query/create/$', views.imageQueryCreateView, name='create'),
	# ex: /imageCrawler/edit/model-id
	url(r'^query/edit/(?P<pk>\d+)$', views.ImageQueryUpdateView.as_view(), name='edit'),
	# ex: /imageCrawler/delete/model-id
	url(r'^query/delete/(?P<pk>\d+)$', views.ImageQueryDeleteView.as_view(), name='delete'),
	url(r'^query/read/(?P<pk>\d+)$', views.imageQueryReadView, name='read'),
	# ex: /imageCrawler/image/model-id
	url(r'^image/(?P<pk>\d+)$', views.ImageResultView.as_view(), name='image'),
	url(r'^image/all/$', views.ImageResultListView.as_view(), name='imageall')
)