from django import forms
from apps.professores.models import Professor


class ProfessorModelForm(forms.ModelForm):

    class Meta:
        model = Professor
        fields = '__all__'
