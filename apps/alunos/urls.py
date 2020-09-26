from django.urls import path
from .views import AlunoView, CreateAlunoView, UpdateAlunoView, DeleteAlunoView

urlpatterns = [
    path('', AlunoView.as_view(), name='aluno_list'),
    path('add/', CreateAlunoView.as_view(), name='add_aluno'),
    path('<int:pk>/update/', UpdateAlunoView.as_view(), name='upd_aluno'),
    path('<int:pk>/delete/', DeleteAlunoView.as_view(), name='del_aluno'),
]