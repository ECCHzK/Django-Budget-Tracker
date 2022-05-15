from django.urls import path
from . import views
from register import views as v

urlpatterns = [
path('', views.home, name='home'),
path('add/', views.add, name='add'),
path('register/', v.register, name='register')
]