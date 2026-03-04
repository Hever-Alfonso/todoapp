from django.urls import path
from . import views

urlpatterns = [
    # GET  /api/todos/  → lista tareas del usuario autenticado
    # POST /api/todos/  → crea una nueva tarea
    path('todos/', views.ToDoListCreate.as_view(), name='todo_list'),

    # GET    /api/todos/<pk>  → detalle de una tarea
    # PUT    /api/todos/<pk>  → actualiza una tarea
    # DELETE /api/todos/<pk>  → elimina una tarea
    path('todos/<int:pk>', views.ToDoRetrieveUpdateDestroy.as_view(), name='todo_RUD'),

    # PUT /api/todos/<pk>/complete  → invierte el estado completed
    path('todos/<int:pk>/complete', views.ToDoToggleComplete.as_view(), name='todo_complete'),

    # POST /api/signup/  → registra usuario y retorna token
    path('signup/', views.signup, name='signup'),

    # POST /api/login/   → autentica usuario y retorna token
    path('login/', views.login, name='login'),
]