from rest_framework import serializers
from todo.models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    """
    Serializer para el modelo ToDo.
    created y completed son de solo lectura:
    - created se asigna automaticamente por el modelo.
    - completed se maneja con el endpoint toggle, no desde creacion.
    """

    created = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()

    class Meta:
        model = ToDo
        fields = ['id', 'title', 'memo', 'created', 'completed']


class ToDoToggleCompleteSerializer(serializers.ModelSerializer):
    """
    Serializer exclusivo para el endpoint de toggle completed.
    Todos los campos son de solo lectura excepto completed,
    que se invierte en perform_update de la vista.
    """

    class Meta:
        model = ToDo
        fields = ['title', 'memo', 'created', 'completed']
        read_only_fields = ['title', 'memo', 'created', 'completed']