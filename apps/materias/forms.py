from django import forms
from apps.materias.models import Materia


class MateriaModelForm(forms.ModelForm):

    class Meta:
        model = Materia
        fields = '__all__'
