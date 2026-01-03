from django.db import models

class Turma(models.Model):
    ANO_CHOICES = [
        (1, '1º Ano'),
        (2, '2º Ano'),
        (3, '3º Ano'),
    ]

    ano = models.IntegerField(choices=ANO_CHOICES)
    codigo = models.CharField(
                        max_length=1,
                        help_text="Ex. A, B, C ...")
    ativo = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('ano', 'codigo')
        ordering = ['ano', 'codigo']

    def __str__(self):
        return f"{self.ano}º {self.codigo}"
