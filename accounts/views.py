from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from accounts.forms import (
    RegistrationForm,
    EditProfileForm
)



def home(request):
    #Html sayfaya arguman yollama ornek asagida adimi yadiriyorum

    sayilar =[1,2,3,4,5]
    adim ='Semih BULUT'
    args ={'adimkey':adim,'sayikey':sayilar}

    return render(request,'accounts/home.html',args)

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:home'))
    else:
        form = RegistrationForm()

        args = {'form': form}
        return render(request, 'accounts/reg_form.html', args)