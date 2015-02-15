from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
# Create your models here.

class media(models.Model):
	api_id = models.IntegerField()
	type = models.IntegerField()
	name = models.CharField(max_length=100)
	unique_together = (("api_id", "type"),)
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'media'

class usermedia(models.Model):
	user = models.ForeignKey(User)
	media = models.ForeignKey(media)
	status = models.IntegerField()
	class Meta:
		verbose_name_plural = 'usermedia'

admin.site.register(media)
admin.site.register(usermedia)
