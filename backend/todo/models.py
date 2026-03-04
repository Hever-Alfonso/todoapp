from django.db import models
from django.contrib.auth.models import User


class ToDo(models.Model):
    """
    Modelo que representa una tarea en la aplicacion ToDo.
    Cada tarea pertenece a un usuario (ForeignKey a User).
    """

    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    # Se asigna automaticamente al momento de creacion
    created = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    # Usuario que creo la tarea. Si se borra el usuario, se borran sus tareas.
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title