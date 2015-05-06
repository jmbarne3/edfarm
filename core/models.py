from django.db import models
import datetime

# Create your models here.
class ContentMixin(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(max_length=75)

	class Meta:
		abstract = True

class ExpirationMixin(models.Model):
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	@property
	def active(self):
	    if start_date >= datetime.now() and end_date < datetime.now():
	    	return True
	    else:
	    	return False

	class Meta:
		abstract = True
	

class Centerpiece(ContentMixin, ExpirationMixin):
	image = models.ImageField()

class Announcement(ContentMixin, ExpirationMixin):
	content = models.TextField()
