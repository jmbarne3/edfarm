from django.db import models

# Create your models here.
class Produce(models.Model):
	name = models.CharField(max_length=255)
	plural_name = models.CharField(max_length=255, null=True, blank=True)
	description = models.TextField()
	image = models.ImageField()

	@property
	def plural(self):
	    if self.plural_name:
	    	return self.plural_name
	    else:
	    	return self.name + 's'
	

	class Meta:
		verbose_name_plural = 'Produce'

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name

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
	produce = models.ForeignKey(Produce)
	unit_count = models.IntegerField()
	unit_type = models.ForeignKey(UnitType)
	name_override = models.CharField(max_length=255, blank=True, null=True)
	active = models.BooleanField(default=True)
	regular_price = models.DecimalField(max_digits=8, decimal_places=2)
	sales = models.ManyToManyField(Sale)

	def __str__(self):
		if self.unit_count > 1:
			return str(self.unit_count) + ' ' + self.unit_type.plural + ' ' + self.produce.plural
		else:
			return str(self.unit_count) + ' '  + self.unit_type.name + ' ' + self.produce.name

	def __unicode__(self):
		if self.unit_count > 1:
			return str(self.unit_count) + ' ' + self.unit_type.plural + ' ' + self.produce.plural
		else:
			return str(self.unit_count) + ' ' + self.unit_type.name + ' ' + self.produce.name

class Bundle(models.Model):
	name = models.CharField(max_length=255)
	products = models.ManyToManyField(Product)
	image = models.ImageField()
	sales = models.ManyToManyField(Sale)


