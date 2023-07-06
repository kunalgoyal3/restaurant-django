from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from foodapp.models import *

def receipe(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        price = data.get('price')

        print(name)
        print(description)
        print(price)

        result = food(name=name,description=description, price=price)
        result.save()

        return redirect('/')
    passforview=food.objects.all();
    context={'passforview':passforview}
    return render(request, 'receipe.html', context)  # Pass an empty dictionary as the context

def deleterecord(request, record_id):
    deleteitem = food.objects.get(id=record_id)
    deleteitem.delete()
    return redirect('/')


def updaterecord(request, record_id):
    todo = food.objects.get(id=record_id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')

        print(name)
        description = data.get('description')
        price = data.get('price')
        todo.name = name
        todo.description = description
        todo.price = price
        todo.save()
        return redirect('/')


    passforview = get_object_or_404(food, id=record_id)
    context = {'passforview': passforview}
    return render(request, 'update.html', context)