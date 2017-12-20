from django.shortcuts import redirect

def girise_yonlendir(request):
    return redirect('/account/login')