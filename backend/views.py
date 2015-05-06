from django.shortcuts import render

from core.models import *
from retail.models import *

from django.views.generic.base import TemplateView

# Create your views here.
class ManagerHomeView(TemplateView):
	template_name = 'manager-home-view.html'