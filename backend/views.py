from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from datetime import date

from backend.forms import *

from core.models import *
from retail.models import *

from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView

from django.forms.models import modelformset_factory, inlineformset_factory, formset_factory

# Create your views here.
class ManagerHomeView(TemplateView):
	template_name = 'manager-home-view.html'

class HomePageUpdate(TemplateView):
	template_name = 'manager-home-page-view.html'

	def get_context_data(self, **kwargs):
		context = super(HomePageUpdate, self).get_context_data(**kwargs)
		context['centerpieces'] = Centerpiece.objects.filter(end_date__gt=date.today())
		context['announcements'] = Announcement.objects.filter(end_date__gt=date.today())
		return context

class CenterpieceCreateView(CreateView):
	model = Centerpiece
	success_url = reverse_lazy('manager-home-page')
	template_name = 'manager-centerpiece-create-view.html'
	fields = ['title', 'start_date', 'end_date', 'image']

class CenterpieceUpdateView(UpdateView):
	model = Centerpiece
	success_url = reverse_lazy('manager-home-page')
	template_name = 'manager-centerpiece-update-view.html'
	fields = ['title', 'start_date', 'end_date', 'image']

class AnnouncementCreateView(CreateView):
	model = Announcement
	success_url = reverse_lazy('manager-home-page')
	template_name = 'manager-announcement-create-view.html'
	fields = ['title', 'start_date', 'end_date', 'content']

class AnnouncementUpdateView(UpdateView):
	model = Announcement
	success_url = reverse_lazy('manager-home-page')
	template_name = 'manager-announcement-update-view.html'
	fields = ['title', 'start_date', 'end_date', 'content']

# Products

class ProductListView(ListView):
	model = Product
	template_name = 'manager-product-list-view.html'

class ProductCreateView(CreateView):
	model = Product
	success_url = reverse_lazy('manager-product-list')
	template_name = 'manager-product-create-view.html'
	fields = ['name', 'plural_name', 'description', 'image']

class ProductUpdateView(UpdateView):
	model = Product
	success_url = reverse_lazy('manager-product-list')
	template_name = 'manager-product-update-view.html'
	fields = ['name', 'plural_name', 'description', 'image']

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)

		prices = Price.objects.filter(product=self.object)

		price_form = PriceUpdateFormSet(instance=self.object)

		return self.render_to_response(
			self.get_context_data(form=form,
									price_form=price_form
			)
		)

	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form_class = self.get_form_class()
		form = self.get_form(form_class)

		price_form = PriceUpdateFormSet(self.request.POST, instance=self.object)

		if form.is_valid():
			if price_form.is_valid():
				price_form.save()
			else:
				return self.render_to_response(
					self.get_context_data(form=form,
											price_form=price_form,
											errors=price_form.errors
					)
				)
			return self.render_to_response(
							self.get_context_data(form=form,
													price_form=price_form
							)
						)
		else:
			return self.render_to_response(
							self.get_context_data(form=form,
													price_form=price_form,
													errors=form.errors
							)
						)
