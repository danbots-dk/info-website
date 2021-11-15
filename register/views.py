# views.py
from django.shortcuts import render, redirect
from register.forms import  RegisterForm, DentistProfileForm, InvestorProfileForm
from django.contrib.auth.models import Group


def registerDentist(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = DentistProfileForm(request.POST)
        if (form.is_valid() and profile_form.is_valid()):
            user = form.save()
            group = Group.objects.get(name='Dentist')
            user.groups.add(group)
            print('dentist')
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("/home")
    else:

        profile_form = DentistProfileForm()
        form = RegisterForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, "register/regdentist.html", context)



def registerInvestor(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        profile_form = InvestorProfileForm(request.POST)
        if (form.is_valid() and profile_form.is_valid()):
            user = form.save()
            group = Group.objects.get(name='Investor')
            user.groups.add(group)
            print('investor')
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("/home")
    else:

        profile_form = InvestorProfileForm()
        form = RegisterForm()

    context = {'form': form, 'profile_form': profile_form}
    return render(request, "register/reginvestor.html", context)


