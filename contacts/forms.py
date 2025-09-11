from django import forms
from .models import EmergencyContact
import re

class EmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        fields = ['name', 'phone_number', 'location', 'address', 'category', 'description', 'latitude', 'longitude']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'phone_number': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'location': forms.TextInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'address': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'rows': 4}),
            'description': forms.Textarea(attrs={'class': 'w-full py-4 px-6 rounded-xl', 'rows': 4}),
            'category': forms.Select(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'latitude': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
            'longitude': forms.NumberInput(attrs={'class': 'w-full py-4 px-6 rounded-xl'}),
        }

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        # Basic phone number validation (e.g., +1234567890 or 123-456-7890)
        if not re.match(r'^\+?\d{9,15}$|^[\d-]{10,15}$', phone_number):
            raise forms.ValidationError("Enter a valid phone number (e.g., +1234567890 or 123-456-7890).")
        return phone_number