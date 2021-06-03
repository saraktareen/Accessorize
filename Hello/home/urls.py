from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("" , views.index, name ='home'), #takes you to the views.py page and to the index function
    path("about" , views.about, name = 'about'), #takes you to the views.py page and to the about function
    path("bracelets" , views.bracelets, name = 'bracelets'), #takes you to the views.py page and to the services function
    path("earrings" , views.earrings, name = 'earrings'),
    path("rings" , views.rings, name = 'rings'),
    path("contact" , views.contact, name = "contact") #takes you to the views.py page and to the contact function
]