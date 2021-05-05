from django.db import models

class About(models.Model):
    title=models.CharField(max_length=100)
    description_main=models.TextField()
    description_sub=models.TextField()
    content_sub=models.ForeignKey('SubDescription',on_delete=models.SET_NULL,null=True)
    image=models.ImageField(upload_to='about/', blank=True,null=False)

    class Meta:
        verbose_name='About'
        verbose_name_plural='About'

    def __str__(self):
        return self.title


class SubDescription(models.Model):
    name=models.CharField(max_length=100)

    class Meta:
        verbose_name='About Sub-descriptions'
        verbose_name_plural='About Sub-descriptions'

    def __str__(self):
        return self.name
