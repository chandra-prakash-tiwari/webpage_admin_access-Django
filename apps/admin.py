from django.contrib import admin

from apps import models 


myModels=[models.HomeSlider, models.Services, models.OurWorld]
admin.site.register(myModels)