from django.db import models

# Create your models here.
class Post(models.Model):
    Estados_permitidos = [
    ('borrador', 'Borrador'),
    ('publicado', 'Publicado'),
    ('archivado', 'Archivado')
    ]
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=Estados_permitidos, default='borrador')
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
