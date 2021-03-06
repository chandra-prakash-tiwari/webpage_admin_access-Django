# Generated by Django 4.0.1 on 2022-01-20 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_rename_img_services_image_services_redirecturl_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurWorld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Blog'), (2, 'Events')])),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='our-world/')),
                ('redirecturl', models.CharField(max_length=50)),
                ('created_by', models.CharField(max_length=50)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'our_world',
            },
        ),
    ]
