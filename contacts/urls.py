# contacts/urls.py
from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.emergency_contacts, name='emergency_contacts'),
    path('<str:location>/', views.emergency_contacts, name='emergency_contacts_by_location'),
    path('add/', views.add_contact, name='add_contact'),
    path('search/', views.search_contacts, name='search_contacts'),
]
