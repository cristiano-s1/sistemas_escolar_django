from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.materias.models import Materia


# Lista
class MateriaView(ListView):
    models = Materia
    template_name = 'materias/materia_list.html'
    queryset = Materia.objects.all()
    context_object_name = 'materias'


# Cadastrar
class CreateMateriaView(CreateView):
    model = Materia
    template_name = 'materias/materia_form.html'
    fields = ['nome_materia', 'descricao']
    success_url = reverse_lazy('materia_list')


# Atualizar
class UpdateMateriaView(UpdateView):
    model = Materia
    template_name = 'materias/materia_form.html'
    fields = ['nome_materia', 'descricao']
    success_url = reverse_lazy('materia_list')


# Deletar
class DeleteMateriaView(DeleteView):
    model = Materia
    template_name = 'materias/materia_del.html'
    success_url = reverse_lazy('materia_list')

