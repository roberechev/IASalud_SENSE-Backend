from django.db import models

# Create your models here.
class Hospital(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    numBoxes = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)