from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import TemplateView,ListView,DetailView
from django.views.generic.edit import DeleteView,UpdateView
from django import template

from imageCrawler.models import ImageResult,ImageQuery,ImageQueryForm

# index
def index(request):
	return render(request, 'imageCrawler/index.html', {})

# query view
class ImageQueryListView(ListView):
	model = ImageQuery
	def get_query_set(self):
		return ImageQuery.objects.all()

class ImageResultListView(ListView):
	model = ImageResult
	def get_query_set(self):
		return ImageResult.objects.all()

# image view
class ImageResultView(DetailView):
	model = ImageResult

def imageQueryCreateView(request):
	if request.method == 'POST': 
		form = ImageQueryForm(request.POST) 
		if form.is_valid():
			image_query = form.save()
			return HttpResponseRedirect(reverse_lazy('read', kwargs={'pk': image_query.id})) 
		else:
			return render(request, 'imageCrawler/imagequery_form.html', {'form':form,'fromview':True})
	else:
		return render(request, 'imageCrawler/imagequery_form.html', {'fromview':True})

def imageQueryReadView(request, pk):
	return render(request, 'imageCrawler/imagequery_form.html', {
		'read_only': True,
		'object': ImageQuery.objects.get(pk=pk),
	})

class ImageQueryUpdateView(UpdateView):
	model=ImageQuery
	success_url=reverse_lazy('all')

class ImageQueryDeleteView(DeleteView):
	model = ImageQuery
	success_url = reverse_lazy('all')

def delAll(request):
	ImageQuery.objects.all().delete();
	ImageResult.objects.all().delete();
	return render(request, 'imageCrawler/index.html', {})

def imageResultOnly(request, pk):
	image = ImageResult.objects.get(pk=pk)
	return render(request, 'imageCrawler/imageresult.html', {'image':image})