from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator
from .models import EmergencyContact
from .forms import EmergencyContactForm

def is_admin(user):
    return user.is_superuser

def emergency_contacts(request, location=None, category=None):
    contacts = EmergencyContact.objects.filter(is_verified=True)  # Only show verified contacts
    if location:
        contacts = contacts.filter(location__icontains=location)
    if category:
        contacts = contacts.filter(category=category)

    # Pagination: 10 contacts per page
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = EmergencyContact.CATEGORY_CHOICES
    return render(request, 'contacts/contacts.html', {
        'page_obj': page_obj,
        'location': location,
        'category': category,
        'categories': categories,
    })

@login_required
@user_passes_test(is_admin)
def add_contact(request):
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.created_by = request.user
            contact.is_verified = request.user.is_superuser  # Auto-verify for admins
            contact.save()
            return redirect('contacts:emergency_contacts')
    else:
        form = EmergencyContactForm()
    return render(request, 'contacts/add_contact.html', {'form': form})

def search_contacts(request):
    query = request.GET.get('location', '')
    category = request.GET.get('category', '')
    contacts = EmergencyContact.objects.filter(is_verified=True)
    if query:
        contacts = contacts.filter(location__icontains=query)
    if category:
        contacts = contacts.filter(category=category)

    # Pagination
    paginator = Paginator(contacts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = EmergencyContact.CATEGORY_CHOICES
    return render(request, 'contacts/searchContacts.html', {
        'page_obj': page_obj,
        'query': query,
        'category': category,
        'categories': categories,
    })

@login_required
@user_passes_test(is_admin)
def edit_contact(request, pk):
    contact = EmergencyContact.objects.get(pk=pk)
    if request.method == 'POST':
        form = EmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('contacts:emergency_contacts')
    else:
        form = EmergencyContactForm(instance=contact)
    return render(request, 'contacts/edit_contact.html', {'form': form, 'contact': contact})

@login_required
@user_passes_test(is_admin)
def delete_contact(request, pk):
    contact = EmergencyContact.objects.get(pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('contacts:emergency_contacts')
    return render(request, 'contacts/delete_contact.html', {'contact': contact})