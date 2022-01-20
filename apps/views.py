from statistics import mode
from django.shortcuts import render
from . import models

def Home(request):
    context={
        "homesliders":models.HomeSlider.objects.all(),
        "services":models.Services.objects.all(),
        "contents":models.OurWorld.objects.all(),
    }
    return render(request, "home.html", context )
