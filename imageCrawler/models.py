from django import forms
from django.forms import ModelForm
from django.db import models

from imageCrawler import image_crawler

# query class
class ImageQuery(models.Model):
	search_query=models.CharField("",max_length=200)
	def __unicode__(self):
		return self.search_query
	def save(self, *args, **kwargs):
		super(ImageQuery, self).save(*args, **kwargs)
		try:
			image_map = image_crawler.request(self.search_query)
		except TypeError:
			image_map = {}
		for t,i in image_map.iteritems():
			self.imageresult_set.create(title=t,image_file=i)
		return self

# image class
class ImageResult(models.Model):
	title = models.CharField(max_length=100)
	image_file = models.TextField(editable=False)
	query = models.ForeignKey(ImageQuery)
	create_date = models.DateTimeField("datetime of image save", auto_now_add=True)
	@property 
	def image_url( self ):
		try:
			return "data:image/png;base64,%s" % self.image_file    
		except IOError:
			return base64.decode(self.image_file)
	def __unicode__(self):
		return self.title

class ImageQueryForm(ModelForm):	
	class Meta:
		model = ImageQuery
		fields = ['search_query']