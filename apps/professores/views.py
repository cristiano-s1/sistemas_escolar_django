from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.professores.models import Professor


# Lista
class ProfessorView(ListView):
    models = Professor
    template_name = 'professores/professor_list.html'
    queryset = Professor.objects.all()
    context_object_name = 'professores'


# Cadastrar
class CreateProfessorView(CreateView):
    model = Professor
    template_name = 'professores/professor_form.html'
    fields = ['numero_aulas', 'Funcionario', 'Materia']
    success_url = reverse_lazy('professor_list')


# Atualizar
class UpdateProfessorView(UpdateView):
    model = Professor
    template_name = 'professores/professor_form.html'
    fields = ['numero_aulas', 'Funcionario', 'Materia']
    success_url = reverse_lazy('professor_list')


# Deletar
class DeleteProfessorView(DeleteView):
    model = Professor
    template_name = 'professores/professor_del.html'
    success_url = reverse_lazy('professor_list')

