# Generated by Django 3.0.7 on 2021-05-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_shopsdelhi'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopsChennai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Images/Chennai/Events')),
                ('location', models.TextField()),
                ('hreftag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShopsKolkata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Images/Kolkata/Events')),
                ('location', models.TextField()),
                ('hreftag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ShopsMumbai',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='Images/Mumbai/Events')),
                ('location', models.TextField()),
                ('hreftag', models.TextField()),
            ],
        ),
    ]
