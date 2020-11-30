from django.http import HttpResponse
from django.shortcuts import render
from .models import Person
from .forms import PersonForm


def index(request):
    return HttpResponse("Hello, world!")

def hello_world(request):
    return render(request, 'hello_world.html', {})

def register(request):
    return render(request, 'register.html', {"form":PersonForm()})

def registered(request):
    form = PersonForm(request.POST)
    if form.is_valid():
        form.save()
    print(form)
    context = {
        'fname':form.cleaned_data['fname'],
        'lname':form.cleaned_data['lname']
    }
    return render(request, 'registered.html', context)


def listall(request):
	all_entries = Person.objects.all()
	return render(request, 'listall.html', {"persons":all_entries})


