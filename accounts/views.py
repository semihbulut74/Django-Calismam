from django.shortcuts import render, HttpResponse


def home(request):
    #Html sayfaya arguman yollama ornek asagida adimi yadiriyorum

    sayilar =[1,2,3,4,5]
    adim ='Semih BULUT'
    args ={'adimkey':adim,'sayikey':sayilar}



    return render(request,'accounts/home.html',args)