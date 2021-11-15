from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import DentistProfile, InvestorProfile
from django_countries.fields import CountryField
from django.contrib.auth.models import Group

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ["username","email", "first_name", "last_name", "password1", "password2"]
        help_texts ={
            'password1': ('bla'),
        }
    def save(self, commit=True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        # group = Group.objects.get(name='Dentist')
        # user.groups.add(group)

        if commit:
            user.save()
        return user


class InvestorProfileForm(forms.ModelForm):
    country = CountryField(blank_label='(select country)')
    class Meta:
        model = InvestorProfile
        fields = ['country', 'stockInvestor', 'startupInvestor', 'profession', 'investmentlevel','investorage']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.country =  self.cleaned_data['country']
        user.stockInvestor = self.cleaned_data['stockInvestor']
        user.startupInvestor = self.cleaned_data['startupInvestor']
        user.profession = self.cleaned_data['profession']
        user.investmentlevel = self.cleaned_data['investmentlevel']
        user.investorage = self.cleaned_data['investorage']
        # group = Group.objects.get(name='Investor')
        # user.groups.add(group)
        if commit:
            user.save()
        return user


class DentistProfileForm(forms.ModelForm):
    class Meta:
        model = DentistProfile
        fields = ['country', 'occupation', 'usedios', 'interest', 'dentistage', 'hasclinic']

    def save(self, commit=True):
        user = super().save(commit=False)

        user.country =  self.cleaned_data['country']
        user.occupation = self.cleaned_data['occupation']
        user.usedios = self.cleaned_data['usedios']
        user.interest = self.cleaned_data['interest']
        user.dentistage = self.cleaned_data['dentistage']
        user.hasclinic = self.cleaned_data['hasclinic']

        if commit:
            user.save()
        return user
