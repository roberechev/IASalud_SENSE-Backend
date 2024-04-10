from django.db import models
from apps.registros.models import Registro

class Sensor(models.Model):
    id_dispositivo_th = models.CharField(max_length=250, blank=True)
    nombre = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=100, blank=True)
    
    #valor = models.CharField(max_length=100, blank=True)
    registros = models.ManyToManyField(Registro)
    
    ultimo_registro = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    eliminado = models.BooleanField(default=False)
    
    def soft_delete(self):
        self.eliminado = True
        self.save()

    def restore(self):
        self.eliminado = False
        self.save()

    @classmethod
    def objetos_eliminados(cls):
        return cls.objects.filter(eliminado=True)

    @classmethod
    def objetos_no_eliminados(cls):
        return cls.objects.filter(eliminado=False)
