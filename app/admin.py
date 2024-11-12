from django.contrib import admin
from .models import *


# Definir as classes de inline
class CidadeInline(admin.TabularInline):
    model = Cidade # Modelo relacionado
    extra = 1 # Quantidade de formulários em branco


class LivroInline(admin.TabularInline): # Formulário em tabela
    model = Livro
    extra = 1


class EmprestimoInline(admin.StackedInline): # Formulário em pilha
    model = Emprestimo
    extra = 1


class UFAdmin(admin.ModelAdmin):
    list_display = ("sigla",)
    search_fields = ("sigla",)
    ordering = ("sigla",)
    inlines = [CidadeInline]


# Definir as classes de administração
class CidadeAdmin(admin.ModelAdmin):
    list_display = ("nome", "uf")
    list_filter = ("uf",)
    search_fields = ("nome",)
    ordering = ("nome",)


class GeneroAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    list_filter = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)
    inlines = [LivroInline]


class AutorAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    list_filter = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)
    inlines = [LivroInline]


class EditoraAdmin(admin.ModelAdmin):
    list_display = ("nome",)
    list_filter = ("nome",)
    search_fields = ("nome",)
    ordering = ("nome",)
    inlines = [LivroInline]


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "telefone")
    list_filter = ("nome", "email")
    search_fields = ("nome", "email")
    ordering = ("nome", "email")


class LivroAdmin(admin.ModelAdmin):
    list_display = ("autor", "editora", "genero") # Campos a serem exibidos
    list_filter = ("autor", "editora", "genero") # Campos para filtragem
    search_fields = ("autor", "editora", "genero") # Campos para busca
    ordering = ("autor", "editora", "genero") # Campos para ordenação
    inlines = [EmprestimoInline] # Incluir empréstimos no formulário


class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "livro", "data_sai", "data_ent")
    list_filter = ("usuario", "livro")
    search_fields = ("usuario", "livro")
    ordering = ("usuario", "livro")
    # inlines = [LivroInline]


# Registrar as classes no ambiente administrativo
admin.site.register(UF, UFAdmin)
admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Genero, GeneroAdmin)
admin.site.register(Autor, AutorAdmin)
admin.site.register(Editora, EditoraAdmin)
admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Livro, LivroAdmin)
admin.site.register(Emprestimo, EmprestimoAdmin)
