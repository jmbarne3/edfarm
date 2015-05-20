from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from datetime import date

from core.models import *
from retail.models import *

from django.views.generic.base import TemplateView, View
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView, CreateView

from django.forms.models import modelformset_factory, inlineformset_factory

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
	fields = ['name', 'plural_name', 'description', 'image', 'regular_price']

class ProductUpdateView(UpdateView):
	model = Product
	success_url = reverse_lazy('manager-product-list')
	template_name = 'manager-product-update-view.html'
	fields = ['name', 'plural_name', 'description', 'image', 'regular_price']

