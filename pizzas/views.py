from django.shortcuts import render, redirect

from .models import Pizza
from .forms import *

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    pizzas = Pizza.objects.all()
    context = {'Menu': pizzas}
    return render(request, 'pizzas/Menu.html', context)

def pizza(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = Topping.objects.filter(pizza=pizza).order_by('pizza_id')

    context = {'pizza': pizza, 'toppings': toppings}
    return render(request, 'pizzas/pizza.html', context)


def new_comment(request,pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    if request.method != 'POST':
        forms = CommentForm()
    else:
        forms = CommentForm(data=request.POST)
        if forms.is_valid():
            new_comment = forms.save(commit=False)
            new_comment.pizza = pizza
            new_comment.save()
            return redirect('pizzas:pizza', pizza_id=pizza_id)
        
    context = {'form':forms, 'pizza':pizza}
    return render(request, 'pizzas/new_comment.html', context)


