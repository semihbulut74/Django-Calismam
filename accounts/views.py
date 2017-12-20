from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse


def home(request):
    #Html sayfaya arguman yollama ornek asagida adimi yadiriyorum

    sayilar =[1,2,3,4,5]
    adim ='Semih BULUT'
    args ={'adimkey':adim,'sayikey':sayilar}

    return render(request,'accounts/home.html',args)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(reverse('accounts:login'))
    else:
        form = UserCreationForm()

    return render(request, 'accounts/reg_form.html', {'form': form})