# Generated by Django 3.0.7 on 2020-06-23 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubDescription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'About Sub-descriptions',
                'verbose_name_plural': 'About Sub-descriptions',
            },
        ),
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description_main', models.TextField()),
                ('description_sub', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='about/')),
                ('content_sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='About.SubDescription')),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'About',
            },
        ),
    ]
