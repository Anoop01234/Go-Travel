# Generated by Django 3.0.7 on 2021-04-24 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_chennairestaurants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chennairestaurants',
            name='img',
            field=models.ImageField(upload_to='Images/Chennai/Restaurants'),
        ),
        migrations.AlterField(
            model_name='delhirestaurant',
            name='img',
            field=models.ImageField(upload_to='Images/Delhi/Restaurants'),
        ),
    ]
