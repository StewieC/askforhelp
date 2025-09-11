from django.urls import path
from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.emergency_contacts, name='emergency_contacts'),
    path('<str:location>/', views.emergency_contacts, name='emergency_contacts_by_location'),
    path('category/<str:category>/', views.emergency_contacts, name='emergency_contacts_by_category'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path('search/', views.search_contacts, name='search_contacts'),
]