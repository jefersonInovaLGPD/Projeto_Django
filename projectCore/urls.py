from django.urls import path
from projectCore.views import app_register_customer, login_user, sign_up_user, app

urlpatterns = [
    path('', login_user, name='login'),
    path('sign-up/', sign_up_user, name='sign-up'),
    path('app', app, name='app'),
    path('login/', login_user, name='login'),
    path('register-customer', app_register_customer, name='register-customer'),
]
