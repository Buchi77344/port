from django.urls import path
from base.views import *

urlpatterns = [
    path('',index,name="index"),
    path("submit-contact/", contact_form_submission, name="contact_form_submission"),
    path('contact',contact,name="contact"),
    path('about',about,name="about"),
    path('services',services,name="services"),
    path('portfolio',portfolio,name="portfolio"),
]
