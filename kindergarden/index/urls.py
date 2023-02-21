from django.urls import path

from .views import *

urlpatterns = [
    path('', home, name='home'),
path('contact', contact_view, name='contact'),
path('success/', success_view, name='success'),
path('price/', price, name='price'),
path('people/', RegKidSad, name='people'),
path('kids/', kidkas, name='kids'),
path('registration/', RegisterUser.as_view(), name='registration'),
    path('kindergarden/',Kidbuil.as_view(), name = 'kindergarden')
]