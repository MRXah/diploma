from django.shortcuts import render

from .models import Contact
# Create your views here.


def index(request):
    return render(request, 'literature/index.html')


def about(request):
    return render(request, 'literature/about.html')


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'literature/contacts.html', context={'contacts': contacts})
