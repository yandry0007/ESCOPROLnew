from django import forms
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
	telefono = forms.CharField(widget=forms.TextInput())
	photo = forms.ImageField(required=False)

	def clean(self):
		return self.cleaned_data