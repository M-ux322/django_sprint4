from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('registration_done/', views.registration_done, name='registration_done'),
]
