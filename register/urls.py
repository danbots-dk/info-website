from django.urls import path

from . import views

urlpatterns = [
    path('reginvestor', views.registerInvestor, name='reginvestor'),
    path('regdentist', views.registerDentist, name='regdentist'),
]