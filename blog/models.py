from django.db import models
from django.utils import timezone

# Creo el modelo Post para almacenar los posts del blog en la base de datos.
# Imaginar un modelo como una hoja excell con filas y columnas, donde las características del modelo
# son los nombres de las columnas.
class Post(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    texto = models.TextField()
    fecha_de_creacion = models.DateTimeField(
        default=timezone.now)
    fecha_de_publicacion = models.DateTimeField(
        blank=True, null=True)

    def publicar(self):
        self.fecha_de_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo