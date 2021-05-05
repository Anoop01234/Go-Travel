from django.shortcuts import render
from .models import Contact

def ContactPage(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact_form=Contact(firstname=firstname,lastname=lastname,
                            email=email,subject=subject,message=message)
        contact_form.save()
        context={'messages':"Thank you for contacting us. One of our representatives will contact you shortly!"}
        return render(request,'contact.html',context)
    else:
        return render(request,'contact.html',{})
