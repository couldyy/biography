from django.shortcuts import render, redirect
from .models import *
from django.core.mail import send_mail

# Create your views here.


def home(request):
    return render(request, 'dmitrybiography/index.html')

def send_email(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    mail = send_mail(f"Dear, {name}", 'Thank you for... some text', 'couldzet@gmail.com', [email])
    if not UserEmails.objects.filter(email=email).exists():
        UserEmails.objects.create(email=email)
    return redirect('home')

