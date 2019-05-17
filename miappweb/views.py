from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'miappweb/index.html')
def Frutas(request):
    return render(request, 'miappweb/Frutas.html')
def Verduras(request):
	return render(request, 'miappweb/Verduras.html')
def Contacto(request):
	return render(request, 'miappweb/Contacto.html')