from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

context = {"home_page": "active"}



def sendit(request):
    print('got clicked!')
    send_mail(
        'my subject',
        'besked her',
        'info@lehaff.dk',
        ['samir@lehaff.dk','peter@l-holm.dk'],fail_silently=False
    )
    print('færdig')
    return render(request, 'index.html', context)

