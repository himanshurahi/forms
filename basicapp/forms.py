from django import forms
from django.contrib.auth.models import User
# class FormName(forms.Form):
# 	name = forms.CharField()
# 	email = forms.EmailField()
# 	body = forms.CharField(widget = forms.Textarea)


class NewUser(forms.ModelForm):
	class Meta():
		model = User
		fields = ['username','password','email']



