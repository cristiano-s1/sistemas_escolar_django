from django.urls import path
from .views import FuncionarioView, CreateFuncionarioView, UpdateFuncionarioView, DeleteFuncionarioView

urlpatterns = [
    path('', FuncionarioView.as_view(), name='funcionarios_list'),
    path('add/', CreateFuncionarioView.as_view(), name='add_funcionarios'),
    path('<int:pk>/update/', UpdateFuncionarioView.as_view(), name='upd_funcionarios'),
    path('<int:pk>/delete/', DeleteFuncionarioView.as_view(), name='del_funcionarios'),
]