from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.template import RequestContext


# Create your views here.

def login(request):
    template = loader.get_template('login/login.html')
    if request.method == 'GET':
        return HttpResponse(template.render())
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')

def cadastrar(request):
    #template = loader.get_template('login/cadastrar.html')
    if request.method == 'GET':
        return render(request, 'login/cadastrar.html')
    else:
        username = request.POST.get('nome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username=username, email=email, password=password)
        return HttpResponse('criado')
