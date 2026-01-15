from django.shortcuts import render, redirect, get_object_or_404
from .forms import TurmaForm
from .models import Turma

def criar_turma(request):
    if request.method == 'POST':
        form = TurmaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_turmas')
    else:
        form = TurmaForm()
        
    return render(
        request,
        'turmas/criar_turma.html',
        {'form': form}
    )
    
def listar_turmas(request):
     turmas = Turma.objects.filter(ativo=True)
     return render(
         request,
         'turmas/listar_turmas.html',
         {'turmas': turmas}
     )
     
def listar_alunos_turma(request, turma_id):
    turma = get_object_or_404(Turma, id=turma_id)
    alunos = turma.alunos.filter(ativo=True).order_by('nome')
    
    return render(
        request, 
        'turmas/listar_alunos_turma.html',  
        {
            'turma': turma,
            'alunos': alunos
         })