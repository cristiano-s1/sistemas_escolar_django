from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.turmas.models import Turma


# Lista
class TurmaView(ListView):
    models = Turma
    template_name = 'turmas/turma_list.html'
    queryset = Turma.objects.all()
    context_object_name = 'turmas'


# Cadastrar
class CreateTurmaView(CreateView):
    model = Turma
    template_name = 'turmas/turma_form.html'
    fields = ['letra_turma', 'Professor']
    success_url = reverse_lazy('turma_list')


# Atualizar
class UpdateTurmaView(UpdateView):
    model = Turma
    template_name = 'turmas/turma_form.html'
    fields = ['letra_turma', 'Professor']
    success_url = reverse_lazy('turma_list')


# Deletar
class DeleteTurmaView(DeleteView):
    model = Turma
    template_name = 'turmas/turma_del.html'
    success_url = reverse_lazy('turma_list')

