from django.forms import ModelForm 
from django.db import models
from django import forms
from djapp.apps.users.models import petition


class formPetition(forms.ModelForm):
	class Meta:
		model = petition
		exclude = ('date',)