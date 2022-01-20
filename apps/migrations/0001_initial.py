# Generated by Django 4.0.1 on 2022-01-19 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(upload_to='home-slider/')),
                ('alt', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'home_slider',
            },
        ),
    ]