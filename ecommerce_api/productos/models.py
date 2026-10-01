from django.db import models


class Producto(models.Model):
    CATEGORIA_CHOICES = [
        ("electronica", "Electrónica"),
        ("ropa", "Ropa"),
        ("hogar", "Hogar"),
    ]

    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.BooleanField(default=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.nombre


class Nota(models.Model):
    producto = models.ForeignKey(
        Producto, on_delete=models.CASCADE, related_name="reseñas"
    )
    autor = models.CharField(max_length=80)
    texto = models.TextField()
    puntuacion = models.IntegerField()

    def __str__(self):
        return f"Reseña de {self.autor} para {self.producto.nombre}"