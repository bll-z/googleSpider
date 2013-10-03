from django.core.management.base import BaseCommand, CommandError
from imageCrawler.models import ImageQuery

class Command(BaseCommand):
	help = 'Refreshes the image search'
	def handle(self, *args, **options):
		# cycle through and refresh the queries
		for imagequery in ImageQuery.objects.all():
			# it runs the refresh when you save
			imagequery.save()
			# then make sure it worked
			if imagequery.imageresult_set.all().count() > 0:
				self.stdout.write('Successfully refreshed ImageQuery "%s".' % imagequery.id)
			else:
				self.stdout.write('Error, image retrieval for ImageQuery "%s" was not successful.' % imagequery.id)