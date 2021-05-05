from django.db import models

class Contact(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=50)
    message=models.TextField()

    class Meta:
        verbose_name ='Contact'
        verbose_name_plural ='Contacts'

    def __str__(self):
        return self.firstname
