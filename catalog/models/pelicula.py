from django.db import models
from catalog.models.director import Director
from catalog.models.vendedor import Vendedor  

class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")
    fecha_lanzamiento = models.DateField()
    director = models.ForeignKey(Director, on_delete=models.PROTECT, related_name='peliculas')
    vendedores = models.ManyToManyField(Vendedor, related_name='peliculas', blank=True)
    poster = models.ImageField(upload_to='posters/', null=True, blank=True)

    def __str__(self):
        return self.nombre