from django.db import models
from accountApp.models import Doctor, Patient

# Create your models here.
class Appointment(models.Model):
    reason = models.TextField()
    perscription = models.FileField(blank=True,upload_to='prescriptions/')
    class Status (models.TextChoices):
        PENDING= "Pending", "en attente"
        CONFIRMED= "Confirmed", "confirmé"
        CANCELED= "Canceled", "annulé"
    status = models.CharField(max_length=10, choices=Status.choices,default=Status.PENDING)
    duration_minutes = models.IntegerField(default=30)
    appointment_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE,related_name='appointments')
    patient=models.ForeignKey(Patient,on_delete=models.CASCADE,related_name='appointments')