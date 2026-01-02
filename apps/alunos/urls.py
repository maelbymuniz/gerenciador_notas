from django.urls import path
from .views import listar_alunos

urlpatterns = [
    path('alunos/', listar_alunos, name='listar_alunos')
]
