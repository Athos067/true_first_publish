from django.db import models

# Create your models here.

class Filme(models.Model):
    genero_acao = 'ac'
    genero_ficcao = 'fc'
    genero_comedia = 'cm'
    genero_biografia = 'bg'
    genero_suspense = 'sp'
    genero_romance = 'ro'
    genero_opcoes = [
        (genero_acao, 'Ação'),
        (genero_ficcao, 'Ficção'),
        (genero_comedia, 'Terror'),
        (genero_biografia, 'Biografia'),
        (genero_suspense, 'Suspense'),
        (genero_romance, 'Romance')
    ]

    nome = models.CharField(max_length=120)
    genero = models.CharField(max_length=2, choices=genero_opcoes,default=None)
    sinopse = models.TextField()
    lancamento = models.DateField()
    duracao = models.PositiveIntegerField()
    classificacao_indicativa = models.PositiveIntegerField()
    cartaz = models.ImageField(upload_to = 'media')

    def __str__(self):
        return self.nome