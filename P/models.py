from django.db import models

# Create your models here.
#from __future__ import unicode_literals

class Prescription(models.Model):
	create_time = models.DateTimeField(auto_now=True)
	image_name = models.CharField(max_length=200, blank=True)
	image_json = models.TextField(blank=True)
	image = models.ImageField(upload_to='exhibited_picture/%Y/%m/%d', blank=False)
	update_time = models.DateTimeField(blank=True)
	def __unicode__(self):
		return self.image_name