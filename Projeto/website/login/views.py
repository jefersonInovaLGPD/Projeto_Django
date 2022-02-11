from email.header import Header
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import login as loga
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'login/login.html', context)
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            loga(request, user)
            return redirect('app')
        else: 
           return HttpResponse('deu algo errado ai meu parceiro')


def cadastrar(request):
    #template = loader.get_template('login/cadastrar.html')
    context = {}
    if request.method == 'GET':
        return render(request, 'login/cadastrar.html', context)
    else:
        name = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()

        if user:
            messages.error(request, 'Este e-mail já está cadastrado')
            return redirect('cadastrar')
        
        user = User.objects.create_user(username=email, first_name=name,last_name=sobrenome, password=password)
        messages.success(request, f'{name}, você foi cadastrado com sucesso!!')
        return redirect('login')

@login_required(login_url='/')
def app(request):
    return HttpResponse('Rapaz num é que deu certo')
          
        
        
