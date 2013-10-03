from django.conf.urls import patterns, url

from imageCrawler import views

urlpatterns = patterns('',
	# ex: /imageCrawler/
	url(r'^$', views.index, name='index'),
	# ex: /imageCrawler/query/all/
	url(r'^query/all/$', views.ImageQueryListView.as_view(), name='all'),
	# ex: /imageCrawler/query/all/delete/
	url(r'^query/all/delete/$', views.delAll, name='delete:all'),
	# ex: /imageCrawler/query/create/
	url(r'^query/create/$', views.imageQueryCreateView, name='create'),
	# ex: /imageCrawler/query/edit/model-id
	url(r'^query/edit/(?P<pk>\d+)$', views.ImageQueryUpdateView.as_view(), name='edit'),
	# ex: /imageCrawler/query/delete/model-id
	url(r'^query/delete/(?P<pk>\d+)$', views.ImageQueryDeleteView.as_view(), name='delete'),
	# ex: /imageCrawler/query/read
	url(r'^query/read/(?P<pk>\d+)$', views.imageQueryReadView, name='read'),
	# ex: /imageCrawler/image/model-id
	url(r'^image/(?P<pk>\d+)$', views.ImageResultView.as_view(), name='image'),
	# ex: /imageCrawler/image/all/
	url(r'^image/all/$', views.ImageResultListView.as_view(), name='imageall'),
	# ex: /imageCrawler/image/only/model-id
	url(r'^image/only/(?P<pk>\d+)$', views.imageResultOnly, name='imageonly'),
)