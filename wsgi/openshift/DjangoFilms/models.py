from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class media(models.Model):
	id_api = models.IntegerField()
	type = models.IntegerField()
	name = models.CharField(max_length=100)
#    mediauser = models.ManyToManyField(User, through='seguidas')
	def __unicode__(self):
		return self.name
	class Meta:
		verbose_name_plural = 'media'

class usermedia(models.Model):
	id_user = models.ForeignKey(User)
	id_media = models.ForeignKey(media)
	status = models.IntegerField()
	class Meta:
		verbose_name_plural = 'usermedia'

#admin.site.register(media)