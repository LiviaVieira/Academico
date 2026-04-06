from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),

    path('cidade/', CidadesView.as_view(), name='cidade'),
    path('pessoa/', PessoasView.as_view(), name='pessoa'),
    path('curso/', CursosView.as_view(), name='curso'),
    path('disciplina/', DisciplinasView.as_view(), name='disciplina'),
    path('instituicao/', InstituicoesView.as_view(), name='instituicao'),
    path('matricula/', MatriculasView.as_view(), name='matricula'),
    path('curso-disciplina/', CursoDisciplinasView.as_view(), name='curso_disciplina'),
]