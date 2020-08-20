from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import gettext, activate, get_language

# Create your views here.


def Contact(request):
    my_info = Info.objects.first()
    
    if request.method == 'POST':
        message = request.POST['message']
        email = request.POST['email']
        subject = request.POST['subject']

        send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
        
        )



    return render(request, 'contact/contact.html', {'my_info': my_info})
