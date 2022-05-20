from django.urls import path
from projectCore.views import login_user, sign_up_user, app

urlpatterns = [
    path('', login_user, name='login'),
    path('sign-up/', sign_up_user, name='sign-up'),
    path('app', app, name='app')
]
