from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from django.contrib import messages


class IndexView(View):
    page = "index.html" # Página de destino
    def get(self, request):
        context = {
            "emprestimos": Emprestimo.objects.all(), # Recuperar todos os empréstimos
        } # Dicionário de contexto
        return render(request, self.page, context) # Renderizar a página de destino com o contexto

    def post(self, request):
        pass
