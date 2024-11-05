# contacts/views.py
from django.shortcuts import render, redirect
from .models import EmergencyContact
from .forms import EmergencyContactForm
from django.contrib.auth.decorators import login_required

# View to list emergency contacts
def emergency_contacts(request, location=None):
    if location:
        contacts = EmergencyContact.objects.filter(location__iexact=location)
    else:
        contacts = EmergencyContact.objects.all()

    return render(request, 'contacts/contacts.html', {'contacts': contacts, 'location': location})

# View to add contacts (admin-only)
@login_required
def add_contact(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contacts:emergency_contacts')
    else:
        form = EmergencyContactForm()

    return render(request, 'contacts/add_contact.html', {'form': form})

# In views.py of the emergency contacts app
# from django.shortcuts import render
# from .models import EmergencyContact

def search_contacts(request):
    query = request.GET.get('location', '')  # Get the location query from the request
    if query:
        # Filter contacts based on the location
        contacts = EmergencyContact.objects.filter(location__icontains=query)
    else:
        contacts = EmergencyContact.objects.all()  # If no query, show all contacts

    context = {
        'query': query,
        'contacts': contacts
    }
    return render(request, 'contacts/searchContacts.html', context)
