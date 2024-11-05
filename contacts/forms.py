# contacts/forms.py
from django import forms
from .models import EmergencyContact

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['location', 'name', 'phone_number']
