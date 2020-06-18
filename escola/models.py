from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)

    # ?: Esta faltando colocar uma classe Meta aqui ???
    # class Meta():
    #

    def __str__(self):
        return self.nome
    