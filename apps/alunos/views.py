from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.alunos.models import Aluno


# Lista
class AlunoView(ListView):
    models = Aluno
    template_name = 'alunos/aluno_list.html'
    queryset = Aluno.objects.all()
    context_object_name = 'alunos'


# Cadastrar
class CreateAlunoView(CreateView):
    model = Aluno
    template_name = 'alunos/aluno_form.html'
    fields = ['nome_aluno', 'data_nacimento', 'rg', 'cpf', 'telefone', 'Turma']
    success_url = reverse_lazy('aluno_list')


# Atualizar
class UpdateAlunoView(UpdateView):
    model = Aluno
    template_name = 'alunos/aluno_form.html'
    fields = ['nome_aluno', 'data_nacimento', 'rg', 'cpf', 'telefone', 'Turma']
    success_url = reverse_lazy('aluno_list')


# Deletar
class DeleteAlunoView(DeleteView):
    model = Aluno
    template_name = 'alunos/aluno_del.html'
    success_url = reverse_lazy('aluno_list')

