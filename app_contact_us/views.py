from django.shortcuts import render
from .forms import ContactForm
from .models import Contact


def contact_us(request):
    contact_form = ContactForm(request.POST or None)

    context = {
        'contactForm': contact_form
    }

    if contact_form.is_valid():
        Contact.objects.create(**contact_form.cleaned_data)
        context['send_message'] = True

    return render(request, 'contact_us.html', context)
