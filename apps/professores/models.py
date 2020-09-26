from django.db import models
from apps.funcionarios.models import Funcionario
from apps.materias.models import Materia


# TABELA PROFESSORES
class Professor(models.Model):
    id_professor = models.AutoField(primary_key=True)
    numero_aulas = models.IntegerField()
    Funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)

    def __str__(self):
        return self.Funcionario.nome_funcionario

