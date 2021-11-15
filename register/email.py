from django.core.mail import send_mail


def sendmail():
    send_mail(
        'my subject',
        'besked her',
        'samir@lehaff.dk',
        ['samir@lehaff.dk','peter@l-holm.dk'],fail_silently=False
    )