# Generated by Django 4.0.1 on 2022-01-20 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_ourworld'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourworld',
            name='created_by',
            field=models.CharField(auto_created=True, max_length=50),
        ),
    ]