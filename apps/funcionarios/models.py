from django.db import models


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


# TABELA FUNCIONARIOS
class Funcionario(Base):
    id_funcionario = models.AutoField(primary_key=True)
    nome_funcionario = models.CharField(max_length=45)
    data_nacimento = models.DateField()
    rg = models.CharField(max_length=45)
    cpf = models.CharField(max_length=45)
    telefone = models.CharField(max_length=45)
    salario = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.nome_funcionario
