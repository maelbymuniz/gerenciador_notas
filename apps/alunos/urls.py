from django.urls import path
from .views import criar_aluno, listar_alunos, editar_aluno, inativar_aluno

urlpatterns = [
    path('alunos/', listar_alunos, name='listar_alunos'),
    path('alunos/novo/', criar_aluno, name='criar_aluno'),
    path('alunos/<int:aluno_id>/editar/', editar_aluno, name='editar_aluno'),
    path('alunos/<int:aluno_id>/inativar/', inativar_aluno, name='inativar_aluno')
]
