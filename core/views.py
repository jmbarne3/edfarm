from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from django.contrib.auth import authenticate, login

from .forms import *

# Create your views here.
class HomeView(TemplateView):
	template_name = 'home.html'

class LoginView(FormView):
	template_name = 'login.html'
	form_class = LoginForm

	def form_valid(self, form):
		user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
		if user:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return super(LoginView, self).form_invalid(form)

	def get_success_url(self):
		success_url = self.request.GET['next']
		return success_url

class TypographyView(TemplateView):
	template_name = 'typography.html'
	