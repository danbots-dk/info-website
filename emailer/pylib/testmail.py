from django.core.mail import send_mail

send_mail(
    'first test!',
    'whats up!!',
    'slehaff@gmail.com',
    ['samir@lehaff.dk'],
    fail_silently=False,
)

# send_mail()
