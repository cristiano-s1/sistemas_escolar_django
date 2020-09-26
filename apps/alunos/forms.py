from django import forms
from apps.alunos.models import Aluno


class AlunoModelForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'
