from django.shortcuts import render
from .models import MenuItems, MenuCategory
from django.views.generic import ListView

class MenuPageView(ListView):
    model=MenuItems
    template_name="menu-list.html"
    context_object_name='menu_lists'

    def get_context_data(self,**kwargs):
        context=super(MenuPageView,self).get_context_data(**kwargs)
        context['categories']=MenuCategory.objects.all()
        return context
"""Function based Views"""
"""
def MenuPage(request):
    menu_lists=MenuItems.objects.all()
    categories=MenuCategory.objects.all()
    context={'menu_lists':menu_lists,'categories':categories}

    return render(request,'menu-list.html',context)
"""
