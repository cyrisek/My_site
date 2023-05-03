from django.views.generic import TemplateView, ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse
from .models import Project, Contact, Education, Profile
# Create your views here.


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mateusz = Profile.objects.get(name='Mateusz Urban')
        context['mateusz'] = mateusz
        return context


@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        subject = request.POST['name']
        from_email = request.POST['email']
        message = request.POST['message']

        if not all([subject, from_email, message]):
            return JsonResponse({"message": "All fields are required.", "status": "danger"}, status=201)

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
            contact = Contact.objects.create(
                name=subject, email=from_email, message=message)
            contact.save()
        return JsonResponse({"message": "Email sent successfully.", "status": "success"}, status=201)
    else:
        return JsonResponse({"message": "Connection failed, try again.", "status": "danger"}, status=201)
