from django import forms
from django.contrib.admin import widgets

class CenterpieceForm(forms.Form):
	title = forms.CharField(max_length=255)
	start_date = forms.DateField(widget=widgets.AdminDateWidget())
	end_date = forms.DateField(widget=widgets.AdminDateWidget())
	image = forms.ImageField()

class AnnouncementForm(forms.Form):
	title = forms.CharField(max_length=255)
	start_date = forms.DateField(widget=widgets.AdminDateWidget())
	end_date = forms.DateField(widget=widgets.AdminDateWidget())
	content = forms.CharField(widget=forms.Textarea)