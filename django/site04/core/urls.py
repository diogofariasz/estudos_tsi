from django.urls import path
from .views import cursos, cadastrar_curso, cadastrar_publico, cadastrar_area, editar_curso, remover_curso

urlpatterns = [
    path('cursos/', cursos, name='cursos'),

    path('cadastrar_curso/', cadastrar_curso, name='cadastrar_curso'),
    path('cadastrar_publico/', cadastrar_publico, name='cadastrar_publico'),
    path('cadastrar_area/', cadastrar_area, name='cadastrar_area'),
    
    path('editar_curso/<int:id>/', editar_curso, name='editar_curso'),
    path('remover_curso/<int:id>/', remover_curso, name='remover_curso'),
]