from django.contrib import admin
from django.urls import path
from core.views import index, contact, signUp
from django.contrib.auth import views as auth_views
from .forms import LoginForm


app_name = 'core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('signup/', signUp, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html', authentication_form=LoginForm), name='login'),
]
