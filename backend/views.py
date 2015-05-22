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
	template_name = 'manager-product-create-view.html'
	fields = ['name', 'plural_name', 'description', 'image']

	def form_valid(self, form):
		if self.request.POST:
			price_form = PriceUpdateForm(self.request.POST)
			if form.is_valid() and price_form.is_valid():
				form.save()
				print form.instance
				price = Price(
							regular_price=price_form.cleaned_data['regular_price'],
							unit_designation=price_form.cleaned_data['unit_designation'],
							product=form.instance)
				price.save()
				return super(ProductCreateView, self).form_valid(form)
		else:
			self.get_context_data()

	def get_context_data(self, **kwargs):
		context = super(ProductCreateView, self).get_context_data(**kwargs)
		context['price_form'] = PriceUpdateForm
		return context

	def get_success_url(self, **kwargs):
		return reverse_lazy('manager-product-update',
							args=(),
							kwargs={'pk': self.object.pk})


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

		for f in price_form:
			for field in f:
				print field.name

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

			prices = Price.objects.filter(product=self.object)

			price_form = PriceUpdateFormSet(instance=self.object)

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
