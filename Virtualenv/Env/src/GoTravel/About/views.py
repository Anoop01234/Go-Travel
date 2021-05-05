from django.shortcuts import render
from .models import About
from django.views.generic import ListView

class AboutPageView(ListView):
    model=About
    template_name="about-us.html"
    context_object_name='about_us'

"""Function based Views """
"""
def AboutPage(request):
    about_us=About.objects.all()
    context={'about_us':about_us}
    return render(request,'about-us.html',context)
"""
