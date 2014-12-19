from django.db import models
from datetime import datetime

class Promocion(models.Model):
    titulo= models.CharField(max_length=50)
    cargo_descripcion= models.TextField(blank=True, null=True)
    fecha_registro= models.DateField(default=datetime.now)
    imagen = models.ImageField(upload_to='foto_promociones')  
