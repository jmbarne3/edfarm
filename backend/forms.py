from django.forms import ModelForm

from retail.models import *

from django.forms.models import modelformset_factory, inlineformset_factory, formset_factory

class PriceUpdateForm(ModelForm):
	class Meta:
		model = Price
		fields = ['regular_price', 'unit_designation']

	def __init__(self, *args, **kwargs):
		super(PriceUpdateForm, self).__init__(*args, **kwargs)

		for key in self.fields:
			self.fields[key].required = False

PriceUpdateFormSet = inlineformset_factory(Product, Price, form=PriceUpdateForm, extra=1, can_delete=True)