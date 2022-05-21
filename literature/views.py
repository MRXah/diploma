
from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .models import Contact, Place
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


def places_json(request):
    qs = Place.objects.all()
    places = serializers.serialize('json', qs)

    return HttpResponse(places)


def index(request):
    qs = Place.objects.all()
    places = serializers.serialize('json', qs)

    return render(request, 'literature/index.html', context={'places': places})


def about(request):
    return render(request, 'literature/about.html')


class PlaceDV(DetailView):
    model = Place
    context_object_name = 'place'


class PlaceCV(LoginRequiredMixin, CreateView):
    model = Place
    fields = '__all__'
    success_url = reverse_lazy('index')


def contacts(request):
    contacts = Contact.objects.all()
    return render(request, 'literature/contacts.html', context={'contacts': contacts})
