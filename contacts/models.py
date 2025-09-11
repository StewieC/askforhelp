from django.db import models
from django.contrib.auth.models import User

class EmergencyContact(models.Model):
    CATEGORY_CHOICES = [
        ('hospital', 'Hospital'),
        ('ambulance', 'Ambulance'),
        ('police', 'Police'),
        ('fire', 'Fire Department'),
        ('hotline', 'Emergency Hotline'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)  # E.g., city or region
    address = models.TextField(blank=True)  # Detailed address
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='other')
    description = models.TextField(blank=True)  # E.g., "24/7 trauma center"
    is_verified = models.BooleanField(default=False)
    latitude = models.FloatField(null=True, blank=True)  # For future geolocation
    longitude = models.FloatField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.location} ({self.get_category_display()})"

    class Meta:
        ordering = ['category', 'location', 'name']