from django.urls import path
from .views import TurmaView, CreateTurmaView, UpdateTurmaView, DeleteTurmaView

urlpatterns = [
    path('', TurmaView.as_view(), name='turma_list'),
    path('add/', CreateTurmaView.as_view(), name='add_turma'),
    path('<int:pk>/update/', UpdateTurmaView.as_view(), name='upd_turma'),
    path('<int:pk>/delete/', DeleteTurmaView.as_view(), name='del_turma'),
]