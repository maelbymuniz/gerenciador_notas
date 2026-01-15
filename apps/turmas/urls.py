from django.urls import path
from .views import criar_turma, listar_turmas, listar_alunos_turma

urlpatterns = [
    path('turmas/', listar_turmas, name='listar_turmas'),
    path('turmas/nova/', criar_turma, name='criar_turma'),
    path('turma/<int:turma_id>/alunos/', listar_alunos_turma, name='listar_alunos_turma' )
]
