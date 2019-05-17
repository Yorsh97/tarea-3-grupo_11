from django.contrib import admin
from django.urls import path
from.import views

urlpatterns = [
	path('', views.index, name='index'),
	path('Frutas/', views.Frutas, name='Frutas'),
	path('Verduras/', views.Verduras, name='Verduras'),
	path('Contacto/', views.Contacto, name='Contacto'),
	path('index/', views.index, name='index'),
]