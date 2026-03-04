from rest_framework import generics, permissions
from rest_framework.parsers import JSONParser
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError

from todo.models import ToDo
from .serializers import ToDoSerializer, ToDoToggleCompleteSerializer


class ToDoListCreate(generics.ListCreateAPIView):
    """
    GET  /api/todos/  → retorna la lista de tareas del usuario autenticado.
    POST /api/todos/  → crea una nueva tarea para el usuario autenticado.

    Solo retorna las tareas del usuario que hace la peticion.
    permission_classes exige token valido en Authorization header.
    """

    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Solo retorna las tareas del usuario autenticado, ordenadas por fecha
        user = self.request.user
        return ToDo.objects.filter(user=user).order_by('-created')

    def perform_create(self, serializer):
        # Asigna automaticamente el usuario autenticado al crear la tarea
        serializer.save(user=self.request.user)


class ToDoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/todos/<pk>  → detalle de una tarea.
    PUT    /api/todos/<pk>  → actualiza una tarea.
    DELETE /api/todos/<pk>  → elimina una tarea.

    El usuario solo puede operar sobre sus propias tareas.
    """

    serializer_class = ToDoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # El usuario solo puede ver/editar/borrar sus propias tareas
        user = self.request.user
        return ToDo.objects.filter(user=user)


class ToDoToggleComplete(generics.UpdateAPIView):
    """
    PUT /api/todos/<pk>/complete  → invierte el estado completed de la tarea.

    Si completed=False lo pone en True y viceversa.
    Usa ToDoToggleCompleteSerializer que no expone el campo user.
    """

    serializer_class = ToDoToggleCompleteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return ToDo.objects.filter(user=user)

    def perform_update(self, serializer):
        # Invierte el valor actual de completed
        serializer.instance.completed = not serializer.instance.completed
        serializer.save()


@csrf_exempt
def signup(request):
    """
    POST /api/signup/
    Crea un nuevo usuario y retorna su token de autenticacion.
    Si el username ya existe retorna error 400.
    """
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(
                username=data['username'],
                password=data['password']
            )
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=201)
        except IntegrityError:
            return JsonResponse(
                {'error': 'username taken. choose another username'},
                status=400
            )


@csrf_exempt
def login(request):
    """
    POST /api/login/
    Autentica un usuario existente y retorna su token.
    Si las credenciales son incorrectas retorna error 400.
    """
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(
            request,
            username=data['username'],
            password=data['password']
        )
        if user is None:
            return JsonResponse(
                {'error': 'unable to login. check username and password'},
                status=400
            )
        else:
            try:
                token = Token.objects.get(user=user)
            except Token.DoesNotExist:
                token = Token.objects.create(user=user)
            return JsonResponse({'token': str(token)}, status=200)