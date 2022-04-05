from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('first/', views.firstpage, name='first'),
    path('second/', views.secondpage, name='second'),
    path('third/', views.thirdpage, name='third'),
]