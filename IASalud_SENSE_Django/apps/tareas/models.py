from django.db import models

class Tarea(models.Model):
    nombre = models.TextField(blank=True)
    prioridad = models.CharField(max_length=100, blank=True)
    audio_recordatorio = models.FileField(upload_to='audio/', null=True, blank=True)
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
