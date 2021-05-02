from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'pizzas/index.html')

from .models import Pizza

def pizzas(request):
    pizzas = Pizza.objects.order_by('name')

    context = {'pizzas':pizzas}

    return render(request, 'pizzas/pizzas.html', context)


def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)

    toppings = pizza.topping_set.order_by('name')

    context = {'pizza': pizza, 'toppings': toppings}

    return render(request, 'pizzas/pizza.html', context)
