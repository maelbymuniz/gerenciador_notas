from django.urls import path
from .views import criar_turma, listar_turmas

urlpatterns = [
    path('turmas/', listar_turmas, name='listar_turmas'),
    path('turmas/nova/', criar_turma, name='criar_turma'),
]
