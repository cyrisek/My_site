from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Project, Contact
# Create your views here.


def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {
        "projects": projects
    })


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        subject = request.POST['name']
        from_email = request.POST['email']
        message = request.POST['message']

        info = (f"{message} from: {from_email}")

        send_mail(
            subject,
            info,
            from_email,
            ['cyrisek07@gmail.com'],
            fail_silently=False)
        try:
            existing_contact = Contact.objects.get(email=from_email)
            existing_contact.name = subject
            existing_contact.message = message
            existing_contact.save()
        except Contact.DoesNotExist:
            contact = Contact.objects.create(name=subject, email=from_email, message=message)
            contact.save()
        return JsonResponse({"message": "Email sent successfully.", "status": "success"}, status=201)
    else:
        return JsonResponse({"message": "Connection failed, try again.", "status": "danger"}, status=201)
