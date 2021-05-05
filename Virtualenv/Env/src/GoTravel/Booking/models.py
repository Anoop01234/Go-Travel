from django.db import models
from django.utils import timezone

class TableBook(models.Model):
    date=models.DateField()
    time=models.TimeField()
    person=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=50)
    occasion=models.CharField(max_length=50,blank=True)
    special_request=models.TextField(blank=True)

    class Meta:
        verbose_name="Table Book"
        verbose_name_plural="Table Books"

    def __str__(self):
        return self.name

class EventBook(models.Model):
    date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    number_ticket=models.IntegerField()
    cost_per_ticket=models.DecimalField(max_digits=10, decimal_places=2)
    limit_per_person=models.IntegerField()
    event_name=models.CharField(max_length=50)
    event_description=models.TextField()
    image=models.ImageField(upload_to='events/',blank=True,null=False)

    class Meta:
        verbose_name ="Event Book"
        verbose_name_plural ="Event Books"

    def __str__(self):
        return self.event_name
