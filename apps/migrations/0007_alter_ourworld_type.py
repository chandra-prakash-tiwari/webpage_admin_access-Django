# Generated by Django 4.0.1 on 2022-01-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0006_alter_ourworld_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ourworld',
            name='type',
            field=models.CharField(choices=[('Blog', 'Blog'), ('Events', 'Events')], max_length=10),
        ),
    ]