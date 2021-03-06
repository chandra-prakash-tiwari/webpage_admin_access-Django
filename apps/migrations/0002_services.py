# Generated by Django 4.0.1 on 2022-01-19 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='services/')),
            ],
            options={
                'db_table': 'services',
            },
        ),
    ]
