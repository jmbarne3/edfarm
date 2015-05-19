from django import forms
from django.forms import ModelForm
from django.contrib.admin import widgets

from core.models import *

from django.forms.models import modelformset_factory

class CenterpieceForm(forms.ModelForm):
	class Meta:
		model = Centerpiece
		exclude = ['id', 'slug']

	def save(self, *args, **kwargs):
		centerpiece = super(CenterpieceForm, self).save(*args, commit=False **kwargs)
		centerpiece.slug = centerpiece.generate_slug()
		centerpiece.save()

CenterpieceFormSet = modelformset_factory(Centerpiece, form=CenterpieceForm, extra=1)

class AnnouncementForm(forms.ModelForm):
	class Meta:
		model = Announcement
		exclude = ['id', 'slug']

	def save(self, *args, **kwargs):
		announcement = super(AnnouncementForm, self).save(*args, commit=False, **kwargs)
		announcement.slug = announcement.generate_slug()
		announcement.save()

AnnouncementFormSet = modelformset_factory(Announcement, form=AnnouncementForm, extra=1)
