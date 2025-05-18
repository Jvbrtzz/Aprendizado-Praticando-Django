from django.contrib import admin
from galeria.models import Dados

class DadosAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'email', 'genero')
    search_fields = ('nome', 'idade', 'email')
    list_filter = ('genero',)

# Register your models here.
admin.site.register(Dados, DadosAdmin)
