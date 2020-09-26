from django.urls import path
from .views import ProfessorView, CreateProfessorView, UpdateProfessorView, DeleteProfessorView

urlpatterns = [
    path('professor/', ProfessorView.as_view(), name='professor_list'),
    path('add/', CreateProfessorView.as_view(), name='add_professor'),
    path('<int:pk>/update/', UpdateProfessorView.as_view(), name='upd_professor'),
    path('<int:pk>/delete/', DeleteProfessorView.as_view(), name='del_professor'),
]