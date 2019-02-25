
from rest_framework import serializers, viewsets
from . serializer import AdultdataSerializer
from . models import Adults,Adultdata
from django.http import HttpResponse
from django.shortcuts import render,redirect,reverse
from django.views.decorators.cache import cache_page

@cache_page(60 * 15)
def datatable(request):
    return render(request, "survaider/index.html")

@cache_page(60 * 15)
def charts(request):
    return render(request, "survaider/charts.html")

class AdultdataViewSet(viewsets.ModelViewSet):
    queryset = Adultdata.objects.all()
    serializer_class = AdultdataSerializer