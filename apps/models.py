from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User


ourworldtype = (
    ('Blog', 'Blog'),
    ('Events', 'Events'),
)
class HomeSlider(models.Model):
    src=models.ImageField(upload_to="home-slider/")
    alt=models.CharField(max_length=50)

    class Meta:
        db_table="home_slider"


class Services(models.Model):
    image=models.ImageField(upload_to="services/")
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    redirecturl=models.CharField(max_length=50)

    class Meta:
        db_table="services"


class OurWorld(models.Model):
    type=models.CharField(choices=ourworldtype, max_length=10)
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to="our-world/")
    redirecturl=models.CharField(max_length=50)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table="our_world"