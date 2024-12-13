from django.forms import ModelForm
from .models import Curso, Area, Publico


class AreaForm(ModelForm):
    class Meta:
        model = Area
        fields = ['nome']


class PublicoForm(ModelForm):
    class Meta:
        model = Publico
        fields = ['nome']


class CursoForm(ModelForm):
    class Meta:
        model = Curso
        fields = ['titulo', 'descricao', 'autor', 'vagas', 'area', 'publicos']
