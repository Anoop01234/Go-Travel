# Generated by Django 3.1.7 on 2021-03-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App', '0002_delete_app'),
    ]

    operations = [
        migrations.CreateModel(
            name='DelhiRestaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Delhi/Restaurants/Images')),
                ('location', models.TextField()),
                ('hreftag', models.TextField()),
            ],
        ),
    ]
