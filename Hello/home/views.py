from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.template.context_processors import csrf
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable" : "SARAAAAAAA"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("This is the Homepage") #This will be printed if the default page is referred to 
   
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("This is the About page") #Shows a page with the message printed out

def bracelets(request):
    return render(request, 'bracelets.html')
    #return HttpResponse("This is the Services page") #Shows a page with the message printed out
    
def earrings(request):
    return render(request, 'earrings.html')

def rings(request):
    return render(request, 'rings.html')


def contact(request):
    if request.method == "post":
        name = request.post.get('name')
        email = request.post.get('email')
        phone = request.post.get('phone')
        desc = request.post.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.succcess(request, 'Thank you for contacting us.')
    return render(request, 'contact.html')
    #return HttpResponse("This is the Contact page") #Shows a page with the message printed out


