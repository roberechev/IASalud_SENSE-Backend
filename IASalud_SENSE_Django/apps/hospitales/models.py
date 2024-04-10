from django.db import models
from apps.pacientes.models import Paciente
from apps.boxes.models import Box

class Hospital(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    pacientes = models.ManyToManyField(Paciente)
    boxes = models.ManyToManyField(Box)
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
    