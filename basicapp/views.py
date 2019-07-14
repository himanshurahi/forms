from django.shortcuts import render, HttpResponse, redirect
from . import forms

# Create your views here.

# def form_page(request):
# 	form = forms.FormName()

# 	if request.method == "POST":
# 		form = forms.FormName(request.POST)

# 		if form.is_valid():
# 			print(form.cleaned_data['name'])
# 		else:
# 			return redirect('home')


# 	return render(request, 'forms.html',{'form':form})


def form_page(request):
	form = forms.NewUser()

	if request.method == 'POST':
		form = forms.NewUser(request.POST)

		if form.is_valid():
			form.save()
			return redirect('home')
		else:
			return HttpResponse('error')
	else:
		return render(request,'forms.html',{'form':form})
