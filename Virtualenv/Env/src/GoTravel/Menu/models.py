from django.db import models

class MenuItems(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    category=models.ForeignKey('MenuCategory',on_delete=models.CASCADE)
    price=models.FloatField()
    image=models.ImageField(upload_to='menu/')

    class Meta:
        verbose_name='Menu Item'
        verbose_name_plural='Menu Items'

    def __str__(self):
        return self.name

class MenuCategory(models.Model):
    name=models.CharField(max_length=50)

    class Meta:
        verbose_name='Menu Category'
        verbose_name_plural='Menu Categories'

    def __str__(self):
        return self.name
