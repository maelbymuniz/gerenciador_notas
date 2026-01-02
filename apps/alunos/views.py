from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm

def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
        
    return render(request, 'alunos/criar_aluno.html', {'form': form})

def listar_alunos(request):
    alunos = Aluno.objects.filter(ativo=True)  
    return render(
        request, 
        'alunos/listar_alunos.html' , 
        {'alunos': alunos})

def editar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    
    else:
        form = AlunoForm(instance=aluno)
        
    return render(
        request,
        'alunos/editar_aluno.html',
        {'form': form, 'aluno': aluno}
    )
    
def inativar_aluno(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)
    aluno.ativo = False
    aluno.save()
    
    return redirect('listar_alunos')