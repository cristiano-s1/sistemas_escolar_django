from django import forms
from apps.turmas.models import Turma


class TurmaModelForm(forms.ModelForm):

    class Meta:
        model = Turma
        fields = '__all__'
