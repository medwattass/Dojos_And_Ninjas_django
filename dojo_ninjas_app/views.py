from django.shortcuts import render, redirect, HttpResponse
from .models import Dojo, Ninja


def root(request):
    return redirect('/dojos')


def index(request):
    context = {
        "dojos": Dojo.objects.all()
        }
    return render(request, 'dojos.html', context)


def add_ninja(request):
    context = {
        "dojos": Dojo.objects.all()
        }
    return render(request, 'new_ninja.html', context)


def show_ninjas(request, dojo_id):
    data = {
        "dojo" : Dojo.objects.get(id=dojo_id),
        "ninjas" : Ninja.objects.all()
        }
    return render(request, 'ninjas.html', data)


def create_dojo(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Dojo.objects.create(name=name)
        return redirect('/dojos')
    else:
        return HttpResponse('Method not allowed', status=405)


def create_ninja(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        age = request.POST.get('age')
        dojo_id = request.POST.get('dojo_id')
        dojo = Dojo.objects.get(id=dojo_id)
        Ninja.objects.create(first_name=fname, last_name=lname, age=age, dojo=dojo)
        return redirect('/show_ninjas/{}'.format(int(dojo_id)))
    else:
        return HttpResponse('Method not allowed', status=405)

