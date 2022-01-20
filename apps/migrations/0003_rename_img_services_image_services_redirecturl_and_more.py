# Generated by Django 4.0.1 on 2022-01-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_services'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='img',
            new_name='image',
        ),
        migrations.AddField(
            model_name='services',
            name='redirecturl',
            field=models.CharField(default='/', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.CharField(max_length=50),
        ),
    ]