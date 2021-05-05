from django.db import models

class Chef(models.Model):
    name=models.CharField(max_length=50)
    position=models.CharField(max_length=50)
    description=models.TextField()
    photo=models.ImageField(upload_to='chef/')

    class Meta:
        verbose_name ='Chef'
        verbose_name_plural='Chefs'

    def __str__(self):
        return self.name

class Slider(models.Model):
    image=models.ImageField(upload_to='slider/')
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name='Slider'
        verbose_name_plural='Sliders'

    def __str__(self):
        return self.name
