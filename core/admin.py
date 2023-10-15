from django.contrib import admin
from core.models import Categoria, Editora, Autor, Livro, Compra, ItensCompra

# Register your models here.

admin.site.register(Autor)
admin.site.register(Categoria)
admin.site.register(Editora)
admin.site.register(Livro)


class ItensInline(admin.TabularInline):  # Tu pode usar StackedInline
    model = ItensCompra


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    inlines = (ItensInline,)
