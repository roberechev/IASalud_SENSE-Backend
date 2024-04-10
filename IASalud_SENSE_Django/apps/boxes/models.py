from django.db import models
from apps.sensores.models import Sensor
from apps.pacientes.models import Paciente
from apps.tareas.models import Tarea

class Box(models.Model):
    nombre = models.CharField(max_length=100, blank=True)
    sensores = models.ManyToManyField(Sensor)
    paciente = models.ForeignKey(Paciente, on_delete=models.SET_NULL, null=True, blank=True)
    tareas = models.ManyToManyField(Tarea)
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
