from django.db import models
from apps.professores.models import Professor


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


# TABELA MATERIA
class Turma(Base):
    id_turma = models.AutoField(primary_key=True)
    letra_turma = models.CharField(max_length=45)
    Professor = models.ForeignKey(Professor, on_delete=models.CASCADE)

    def __str__(self):
        return self.letra_turma



