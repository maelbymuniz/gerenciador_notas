from django.shortcuts import render, redirect
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