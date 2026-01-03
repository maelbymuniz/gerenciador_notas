from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=150)
    turma = models.ForeignKey(
        'turmas.Turma',
        on_delete=models.PROTECT,
        related_name='alunos'
    )
    
    ativo = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nome
