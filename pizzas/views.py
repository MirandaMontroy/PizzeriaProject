from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

from .models import Pizza

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)