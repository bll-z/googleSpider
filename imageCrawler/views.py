from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django import template
from imageCrawler import image_crawler

from imageCrawler.models import ImageResult,ImageQuery,ImageQueryForm

# index
def index(request):
	return render(request, 'imageCrawler/index.html', {})

# query view
class ImageQueryListView(ListView):
	model = ImageQuery
	template_name='imageCrawler/queries.html'
	def get_query_set(self):
		return ImageQuery.objects.all()


# query view
class ImageQueryView(DetailView):
	model = ImageQuery
	template_name = 'imageCrawler/query.html'

# image view
class ImageResultView(DetailView):
	model = ImageResult
	template_name = 'imageCrawler/image.html'

# search view
def searchView(request):	
	if request.method == 'POST': 
		form = ImageQueryForm(request.POST) 
		if form.is_valid():
			image_query = form.save()
			image_map = image_crawler.request(image_query.search_query)
			for t,i in image_map.iteritems():
				image_query.imageresult_set.create(title=t,image_file=i)
			return HttpResponseRedirect('/imageCrawler/')
	else:
		return render(request, 'imageCrawler/search.html', {})

class ImageQueryCreate(CreateView):
	model = ImageQuery

class ImageQueryUpdate(UpdateView):
	model = ImageQuery

class ImageQueryDelete(DeleteView):
	model = ImageQuery
