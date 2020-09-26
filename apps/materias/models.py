from django.db import models


class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


# TABELA MATERIA
class Materia(Base):
    id_materia = models.AutoField(primary_key=True)
    nome_materia = models.CharField(max_length=45)
    descricao = models.TextField()

    def __str__(self):
        return self.nome_materia


