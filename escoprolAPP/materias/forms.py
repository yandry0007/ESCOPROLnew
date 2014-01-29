from django import forms

class addProductForm(forms.Form):
	nombre = forms.CharField(widget=forms.TextInput())
	num_horas = forms.CharField(widget=forms.TextInput())
	descripcion = forms.CharField(widget=forms.Textarea())
	foto = forms.ImageField(required=False)

	def clean(self):
		return self.cleaned_data


class ContactForm(forms.Form):
	Email = forms.EmailField(widget=forms.TextInput())
	Titulo = forms.CharField(widget=forms.TextInput())
	Texto = forms.CharField(widget=forms.Textarea())

class LoginForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput())
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))
