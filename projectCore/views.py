from multiprocessing import context
from turtle import title
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from projectCore.models import Customer

# Create your views here.
def login_user(request):
    context = {'title':'Login'}
    if request.method == 'GET':
        return render(request, 'projectCore/login.html', context)
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user:
            login(request, user)
            return redirect('app')
        else: 
           return HttpResponse('deu algo errado ai meu parceiro')

def sign_up_user(request):
    #template = loader.get_template('login/cadastrar.html')
    context = {'title':'Sign-up'}
    if request.method == 'GET':
        return render(request, 'projectCore/cadastrar.html', context)
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
    username = None
    if request.user.is_authenticated:
        username = f"{request.user.first_name} {request.user.last_name}" 
    customers = Customer.objects.all()
    context = {
        'customers':customers,
        'title':'Home',
        'username': username
    }
    return render(request, 'projectCore/home.html', context=context)


@login_required(login_url='/')
def app_register_customer(request):
    username = None
    if request.user.is_authenticated:
        username = f"{request.user.first_name} {request.user.last_name}" 
    context = {
        'title':'Registrar Cliente', 
        'username': username
    }
    if request.method =='GET':
        return render(request, 'projectCore/register_customer.html', context=context)
    else:
        customer_razao_social = request.POST.get('razao_social')
        customer_cnpj = request.POST.get('cnpj')
        customer_fantasy_name = request.POST.get('fantasy_name')
        customer_contact_name = request.POST.get('contact_name')
        customer_contact_email = request.POST.get('contact_email')
        customer_logo = request.POST.get('customer_logo')

        customer = Customer.objects.filter(customer_cnpj=customer_cnpj).first()

        if customer:
            messages.error(request, f'Cliente {customer.customer_fantasy_name} já cadastrado')
            return redirect('register-customer')
        
        customer = Customer.objects.create(
            customer_razao_social=customer_razao_social, customer_cnpj=customer_cnpj,
            customer_fantasy_name=customer_fantasy_name, customer_contact_name=customer_contact_name,
            customer_contact_email=customer_contact_email, customer_logo=customer_logo
        )
        messages.success(request, f'{customer_fantasy_name}, foi cadastrado com sucesso!!')
        return redirect('register-customer')

@login_required(login_url='/')
def customer_view(request, id):
    username = None
    if request.user.is_authenticated:
        username = f"{request.user.first_name} {request.user.last_name}"
    customer = Customer.objects.filter(id=id).first()
    context = {
        'title': customer.customer_fantasy_name,
        'username': username,
        'customer': customer
    }
    return render(request, 'projectCore/customer.html', context)

