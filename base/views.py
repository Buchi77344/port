from django.shortcuts import render, redirect
from . models import *
# Create your views here.
def index(request):
    return render (request, 'index.html')

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


@csrf_exempt  # Only use if you are testing without CSRF token; otherwise, ensure the CSRF token is included.
def contact_form_submission(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        # Simple validation
        if not name or not email or not subject or not message:
            return JsonResponse({"success": False, "error": "All fields are required."}, status=400)

        # Save the message in the database (optional)
        Contact.objects.create(name=name, email=email, subject=subject, message=message)

        return JsonResponse({"success": True, "message": "Message sent successfully!"})

    return JsonResponse({"success": False, "error": "Invalid request method."}, status=405)


def contact(request):
    return render (request, 'contact.html')  


def about(request):
    return render (request, 'about.html')  


def services(request):
    return render (request, 'services.html')


def portfolio(request):
    return render (request, 'portfolio.html')