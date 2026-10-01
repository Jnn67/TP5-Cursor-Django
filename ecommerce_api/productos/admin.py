from django.contrib import admin
from .models import Producto, Nota


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "precio", "stock", "categoria")
    list_filter = ("categoria", "stock")
    search_fields = ("nombre",)


@admin.register(Nota)
class NotaAdmin(admin.ModelAdmin):
    list_display = ("id", "producto", "autor", "puntuacion")
    list_filter = ("producto", "puntuacion")
    search_fields = ("autor", "texto")