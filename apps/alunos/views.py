from django.shortcuts import render
from .models import Aluno

def listar_alunos(request):
    alunos = Aluno.objects.filter(ativo=True)
    
    return render(request, 'alunos/listar_alunos.html' , {'alunos': alunos})