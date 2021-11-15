from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser


# class CustomUser(AbstractUser):
#     mobile = models.CharField(max_length=16)
    # if your additional field is a required field, just add it, don't forget to add 'email' field too.
    # REQUIRED_FIELDS = ['mobile', 'email']
class InvestorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length= 30)
    stockInvestor = models.BooleanField(help_text='Are you an active stock investor?')
    startupInvestor = models.BooleanField(help_text= 'previous startup investor')
    profession = models.CharField(max_length=30)
    investmentlevel = models.IntegerField()
    investorage = models.IntegerField()

    # def __str__(self):
    #     return self.user.first_name

class DentistProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = models.CharField(max_length= 30)
    occupation = models.CharField(max_length=20)
    usedios = models.BooleanField(help_text='have used Intra Oral Scanner')
    interest = models.BooleanField(help_text= 'Considering to buy IOS')
    dentistage = models.IntegerField()
    hasclinic = models.BooleanField()