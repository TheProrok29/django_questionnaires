from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from . import forms 


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required
def settings(request):
    kwargs = {}
    kwargs['basic_data_change_form'] = forms.UserBasicDataChangeForm(prefix='basic_data_change_form', 
    instance=request.user)
    kwargs['password_change_form'] = forms.UserPasswordChangeForm(prefix='password_change_form') 

    return render(request, 'settings.html', kwargs)
    
