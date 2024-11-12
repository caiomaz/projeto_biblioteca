from typing import Any
from django.db import models


# Classe 'UF' para representar as Unidades Federativas
class UF(models.Model):
    sigla = models.CharField(
        max_length=2, # Tamanho máximo da sigla
        verbose_name="Sigla", # Nome da coluna no ambiente administrativo
        unique=True, # A sigla deve ser única
        help_text="Informe a sigla da Unidade Federativa", # Texto de ajuda
        default="--" # Valor padrão
    )

    class Meta:
        verbose_name = "Unidade Federal"  # Nome da classe no singular
        verbose_name_plural = "Unidades Federais"  # Nome da classe no plural

    def __str__(self):
        return self.sigla # Retorna a sigla da UF como string para representar o objeto
    

# Classe 'Cidade' para representar as cidades
class Cidade(models.Model):
    nome = models.CharField(
        max_length=255,
        verbose_name="Nome da Cidade",
        unique=True,
        help_text="Informe o nome da cidade",
        default="--"
    )
    uf = models.ForeignKey(
        UF, # Chave estrangeira para a classe UF
        on_delete=models.CASCADE, # Ação de exclusão em cascata
        verbose_name="Unidade Federal",
        help_text="Selecione a Unidade Federal",
        default=1, # Valor padrão - UF com sigla 'XX'
    )

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"

    def __str__(self):
        return self.nome


# Classe 'Genero' para representar os gêneros literários
class Genero(models.Model):
    nome = models.CharField(
        max_length=255, # Tamanho máximo do nome
        verbose_name="Nome do Gênero", # Nome da coluna no ambiente administrativo
        unique=True, # O nome do gênero deve ser único
        help_text="Informe o nome do gênero literário", # Texto de ajuda
        default="--" # Valor padrão
    )

    class Meta:
        verbose_name = "Gênero"
        verbose_name_plural = "Gêneros"

    def __str__(self):
        return self.nome


# Hiperclasse 'Pessoa' que será uma classe pai
class Pessoa(models.Model):
    nome = models.CharField(
        max_length=255, 
        default="--",
        verbose_name="Nome",
        help_text="Informe o nome"
    )
    email = models.CharField(
        max_length=255, 
        default="--",
        verbose_name="E-mail",
        help_text="Informe o e-mail",
    )
    telefone = models.CharField(
        max_length=20,
        default="--",
        verbose_name="Telefone",
        help_text="Informe o telefone",
    )
    cidade = models.ForeignKey(
        Cidade, 
        on_delete=models.CASCADE, 
        default=1,
        verbose_name="Cidade",
        help_text="Selecione a cidade"
    )

    class Meta:
        abstract = True

    def __str__(self):
        return self.nome


# Superclasse que herda de 'Pessoa' e que representa uma pessoa física
class PessoaFisica(Pessoa):
    cpf = models.CharField(
        max_length=11, 
        default="--",
        verbose_name="CPF",
        help_text="Informe o CPF"
    )
    data_nasc = models.DateField(
        default="2000-01-01", # Data padrão no formato AAAA-MM-DD
        verbose_name="Data de Nascimento",
        help_text="Informe a data de nascimento"
    )

    class Meta:
        abstract = True


# Superclasse que herda de 'Pessoa' e que representa uma pessoa jurídica
class PessoaJuridica(Pessoa):
    cnpj = models.CharField(
        max_length=14, 
        default="--",
        verbose_name="CNPJ",
        help_text="Informe o CNPJ"
    )
    razao_social = models.CharField(
        max_length=255, 
        default="--",
        verbose_name="Razão Social",
        help_text="Informe a razão social"
    )
    data_fund = models.DateField(
        default="2000-01-01",
        verbose_name="Data de Fundação",
        help_text="Informe a data de fundação"
    )

    class Meta:
        abstract = True


# Subclasse 'Autor' que herda de 'PessoaFisica'
class Autor(PessoaFisica):
    pass

    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autores"


# Subclasse 'Editora' que herda de 'PessoaJuridica'
class Editora(PessoaJuridica):

    class Meta:
        verbose_name = "Editora"
        verbose_name_plural = "Editoras"


# Subclasse 'Usuario' que herda de 'PessoaFisica'
class Usuario(PessoaFisica):
    pass

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"


# Classe 'Livro' que representa um livro
class Livro(models.Model):
    nome = models.CharField(
        max_length=255,
        default="--",
        verbose_name="Nome do Livro",
        help_text="Informe o nome do livro"
    )
    genero = models.ForeignKey(
        Genero, 
        on_delete=models.CASCADE,
        verbose_name="Gênero Literário",
        help_text="Selecione o gênero literário",
        default=1
    )
    autor = models.ForeignKey(
        Autor, 
        on_delete=models.CASCADE,
        verbose_name="Autor",
        help_text="Selecione o autor",
        default=1,
    )
    editora = models.ForeignKey(
        Editora, 
        on_delete=models.CASCADE,
        verbose_name="Editora",
        help_text="Selecione a editora",
        default=1,
    )
    preco = models.IntegerField(
        default=0,
        verbose_name="Preço",
        help_text="Informe o preço do livro"
    )
    data_pub = models.DateField(
        default="2000-01-01",
        verbose_name="Data de Publicação",
        help_text="Informe a data de publicação"
    )

    class Meta:
        verbose_name = "Livro"
        verbose_name_plural = "Livros"

    def __str__(self):
        return self.nome


# Classe 'Emprestimo' que representa um empréstimo de um livro
class Emprestimo(models.Model):
    data_ent = models.DateField(
        default="2000-01-01",
        verbose_name="Data de Entrega",
        help_text="Informe a data de entrega"
    )
    data_sai = models.DateField(
        default="2000-01-01",
        verbose_name="Data de Saída",
        help_text="Informe a data de saída"
    )
    usuario = models.ForeignKey(
        Usuario, 
        on_delete=models.CASCADE,
        verbose_name="Usuário",
        help_text="Selecione o usuário",
        default=1   
    )
    livro = models.ForeignKey(
        Livro, 
        on_delete=models.CASCADE,
        verbose_name="Livro",
        help_text="Selecione o livro",
        default=1
    )

    class Meta:
        verbose_name = "Empréstimo"
        verbose_name_plural = "Empréstimos"

    def __str__(self):
        return f"{self.usuario} pegou {self.livro} emprestado em {self.data_sai} e deve devolver em {self.data_ent}"

    