from django.shortcuts import render
from Booking.models import EventBook
from .models import Chef, Slider
from Menu.models import MenuItems, MenuCategory
from django.views.generic import ListView


'''
class IndexPageView(ListView):
    model=EventBook
    template_name="index.html"
    context_object_name="events"

    def get_context_data(self,**kwargs):
        context=super(IndexPageView,self).get_context_data(**kwargs)
        context['sliders']=Slider.objects.all()
        context['meal_lists']=MenuItems.objects.all()
        context['chefs']=Chef.objects.all()
        context['categories']=MenuCategory.objects.all()
        return context

'''
def IndexPage(request):
    events=EventBook.objects.all()
    chefs=Chef.objects.all()
    sliders=Slider.objects.all()
    meal_lists=MenuItems.objects.all()
    categories=MenuCategory.objects.all()
    context={'events':events,'chefs':chefs,'sliders':sliders,
            'meal_lists':meal_lists,'categories':categories}
    return render(request, 'index.html',context)
