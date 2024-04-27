from django.db import models

class Paciente(models.Model):
    numero_historia = models.CharField(max_length=100, blank=True)
    nombre = models.CharField(max_length=250, blank=True)
    genero = models.CharField(max_length=100, blank=True)
    edad = models.CharField(max_length=100, blank=True)
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
