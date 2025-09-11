from django.db import models
from django.contrib.auth.models import User
from contacts.models import EmergencyContact

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=100, choices=[
        ('first_aid', 'First Aid'),
        ('cpr', 'CPR'),
        ('bleeding', 'Bleeding Control'),
        ('other', 'Other Medical Procedures'),
    ], default='other')
    related_contacts = models.ManyToManyField(EmergencyContact, blank=True, related_name='related_articles')

    def __str__(self):
        return self.title