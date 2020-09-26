from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from apps.funcionarios.models import Funcionario


# Lista
class FuncionarioView(ListView):
    models = Funcionario
    template_name = 'funcionarios/funcionarios_list.html'
    queryset = Funcionario.objects.all()
    context_object_name = 'funcionarios'


# Cadastrar
class CreateFuncionarioView(CreateView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_form.html'
    fields = ['nome_funcionario', 'data_nacimento', 'rg', 'cpf', 'telefone', 'salario']
    success_url = reverse_lazy('funcionarios_list')


# Atualizar
class UpdateFuncionarioView(UpdateView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_form.html'
    fields = ['nome_funcionario', 'data_nacimento', 'rg', 'cpf', 'telefone', 'salario']
    success_url = reverse_lazy('funcionarios_list')


# Deletar
class DeleteFuncionarioView(DeleteView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_del.html'
    success_url = reverse_lazy('funcionarios_list')
