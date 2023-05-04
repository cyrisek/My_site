from django.views.generic import TemplateView, FormView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse, FileResponse, Http404
from .models import Contact, Profile
from .forms import ContactForm


class BaseView(TemplateView):
    template_name = 'base.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        mateusz = Profile.objects.get(name='Mateusz Urban')
        context['mateusz'] = mateusz
        form = ContactForm()
        context['form'] = form
        return context


class ContactView(FormView):
    form_class = ContactForm
    template_name = 'contact_form.html'
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        subject = form.cleaned_data['name']
        from_email = form.cleaned_data['email']
        message = form.cleaned_data['message']

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

    def form_invalid(self, form):
        return JsonResponse({"message": "All fields are required.", "status": "danger"}, status=201)


def download_file(request):
    mateusz = get_object_or_404(Profile, name='Mateusz Urban')
    my_cv = mateusz.bio.cv
    print(my_cv)

    response = FileResponse(my_cv)

    return response
