from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html',)
    # return render(request,"index.html")

def about(request):
    return render(request, 'about.html',)
    # return HttpResponse("This Is Aboutpage")

def services(request):
    return render(request, 'services.html',)
    # return HttpResponse("This Is Services page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('first_name')
        name2 = request.POST.get('last_name')
        country = request.POST.get('country')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        contact = Contact(first_name=name, last_name=name2, country=country, phone=phone, subject=subject, date=datetime.today())
        contact.save()
        messages.success(request, "Your message has been sent.")


    return render(request, 'contact.html',)
    # return HttpResponse("This Is Contact page")


