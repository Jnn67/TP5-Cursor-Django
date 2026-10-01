from rest_framework import serializers
from .models import Producto, Nota


class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ["id", "producto", "autor", "texto", "puntuacion"]


class ProductoSerializer(serializers.ModelSerializer):
    resenas = NotaSerializer(source="reseñas", many=True, read_only=True)

    class Meta:
        model = Producto
        fields = ["id", "nombre", "precio", "stock", "categoria", "resenas"]