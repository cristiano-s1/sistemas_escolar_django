from django.db import models
from apps.turmas.models import Turma


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


# TABELA ALUNOS
class Aluno(Base):
    id_aluno = models.AutoField(primary_key=True)
    nome_aluno = models.CharField(max_length=45)
    data_nacimento = models.DateField()
    rg = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    Turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_aluno
