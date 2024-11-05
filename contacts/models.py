# contacts/models.py

from django.db import models


class EmergencyContact(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.location}"

