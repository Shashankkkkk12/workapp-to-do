from django import forms
# it is a magical thing wich will convert your models into forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):

	class Meta:
		model = Task
		fields = '__all__'