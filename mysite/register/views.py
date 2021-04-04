from django.shortcuts import render, redirect
from .forms import Register
'''
For to customize the forms, was used crispy-forms,
what can be installed in this mode:
    pip install django-crispy-forms
'''


# Create your views here.
def register(response):
    if response.method == 'POST':
        form = Register(response.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    else:
        form = Register()
    return render(response, 'register/register.html', {'form':  form})

