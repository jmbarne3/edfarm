from django.shortcuts import render

from core.models import *
from retail.models import *

from .forms import *

from django.views.generic.base import TemplateView, View
from django.views.generic.edit import FormView

# Create your views here.
class ManagerHomeView(TemplateView):
	template_name = 'manager-home-view.html'

class HomePageUpdate(View):

	def get(self, request):
		centerpiece_form = CenterpieceForm(prefix='centerpiece_form')
		announcement_form = AnnouncementForm(prefix='announcement_form')

		context = {
			'centerpiece_form' : centerpiece_form,
			'announcement_form' : announcement_form,
		}

		return render(request, 'manager-home-page-update.html', context)

	def post(self, request):
		centerpiece_form = CenterpieceForm(prefix='centerpiece_form')
		announcement_form = AnnouncementForm(prefix='announcement_form')

		context = {
			'centerpiece_form' : centerpiece_form,
			'announcement_form' : announcement_form,
		}

		return render(request, 'manager-home-page-update.html', context)