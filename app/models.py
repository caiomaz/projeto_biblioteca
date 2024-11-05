from django.db import models

class UF(models.Model):
    sigla = models.CharField(max_length=2, verbose_name='Sigla')

    class Meta:
        verbose_name='Unidade Federal'
        verbose_name_plural='Unidades Federais'

    def __str__(self):
        return self.sigla
    
class Cidade(models.Model):
    nome = models.CharField(max_length=255)
    uf = models.ForeignKey(UF, on_delete=models.CASCADE)

class Genero(models.Model):
    nome = models.CharField(max_length=255)

class Editora(models.Model):
    nome = models.CharField(max_length=255)
    site = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    
class Autor(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

class Livro(models.Model):
    nome = models.CharField(max_length=255)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    editora = models.ForeignKey(Editora, on_delete=models.CASCADE)
    preco = models.IntegerField()
    datapub = models.DateField()

class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.IntegerField()
    data_nasc = models.DateField()
    email = models.CharField(max_length=255)
    telefone = models.IntegerField()
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

class Emprestimo(models.Model):
    dataentrada = models.DateField()
    datasaida = models.DateField()
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)