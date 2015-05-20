from django.db import models

# Create your models here.
class UnitType(models.Model):
	name = models.CharField(max_length=255)
	plural = models.CharField(max_length=255)
	abbreviation = models.CharField(max_length=3)
	abbreviation_plural = models.CharField(max_length=4)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Sale(models.Model):
	sale_price = models.DecimalField(max_digits=8, decimal_places=2)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

	def __str__(self):
		return self.start_date.strftime('%m/%d/%y') + ' ' + str(self.sale_price)

	def __unicode__(self):
		return self.start_date.strftime('%m/%d/%y') + ' ' + str(self.sale_price)


class Product(models.Model):
	name = models.CharField(max_length=255)
	plural_name = models.CharField(max_length=255, null=True, blank=True)
	description = models.TextField()
	image = models.ImageField()
	active = models.BooleanField(default=True)
	regular_price = models.DecimalField(max_digits=8, decimal_places=2)
	sales = models.ManyToManyField(Sale, blank=True)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

class Bundle(models.Model):
	name = models.CharField(max_length=255)
	products = models.ManyToManyField(Product)
	image = models.ImageField()
	sales = models.ManyToManyField(Sale)


