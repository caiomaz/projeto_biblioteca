from django.contrib import admin
from .models import *


class CidadeInline(admin.TabularInline):
    model = Cidade
    extra = 1

class UFAdmin(admin.ModelAdmin):
    inlines = [CidadeInline]

admin.site.register(UF, UFAdmin)
admin.site.register(Cidade)
