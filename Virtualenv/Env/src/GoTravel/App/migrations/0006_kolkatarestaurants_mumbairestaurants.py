# Generated by Django 3.0.7 on 2021-04-30 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_auto_20210424_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='KolkataRestaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Images/Kolkata/Restaurants')),
                ('location', models.TextField()),
                ('hreftag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='MumbaiRestaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Images/Mumbai/Restaurants')),
                ('location', models.TextField()),
                ('hreftag', models.TextField()),
            ],
        ),
    ]
