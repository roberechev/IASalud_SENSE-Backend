from django.db import models

class Registro(models.Model):
    valor = models.CharField(max_length=250, blank=True)
    unidades = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=250, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
