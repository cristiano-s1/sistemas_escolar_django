from django.urls import path
from .views import MateriaView, CreateMateriaView, UpdateMateriaView, DeleteMateriaView

urlpatterns = [
    path('', MateriaView.as_view(), name='materia_list'),
    path('add/', CreateMateriaView.as_view(), name='add_materia'),
    path('<int:pk>/update/', UpdateMateriaView.as_view(), name='upd_materia'),
    path('<int:pk>/delete/', DeleteMateriaView.as_view(), name='del_materia'),
]