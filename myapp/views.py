from django.shortcuts import render, HttpResponse
from myapp.models import Contact
from django.contrib import messages
def index(request):
    return render(request, 'index.html')
    #return HttpResponse("This Is Home Page")

def about(request):
    return render(request, 'aboutus.html')
    #return HttpResponse("This Is About Page")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        messages.success(request, 'Form Submitted Sucessfully')
    return render(request, 'contact.html')
    #return HttpResponse("This Is Contact Page")

def career(request):
    return render(request, 'career.html')
    #return HttpResponse("This Is Career Page")

def home(request):
    return render(request, 'home.html')
    #return HttpResponse("This Is Career Page")


